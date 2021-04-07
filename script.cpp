#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/prctl.h>
#include <fstream>
#include <string>
#include <mutex>
#include <cstdlib>
#include <vector>

std::mutex mutex;

void KillChild(std::vector<pid_t>& childPids){
    for (auto pid : childPids) {
		kill(pid, SIGQUIT);
	}
}

int main(int argc, char** argv, char** envp){

    pid_t subPid;
    int countProc;
    int countIter;
    int i, j;
    FILE* handle;
    std::vector<pid_t> childPids;

    if(argc < 4){
        perror("USAGE fork <message> <count processes> <count interation>\n");
        return 1;
    }

    countProc = atoi(argv[2]);
    countIter = atoi(argv[3]);

    handle = fopen("logfile.log", "a+");
    if(!handle){
        perror("Error open logfile\n");
        return 1;
    }

    for(i = 0; i < countProc; ++i){
        subPid = fork();
        if(subPid == 0){
            for(j = 0; j < countIter; ++j){
                prctl(PR_SET_PDEATHSIG, SIGHUP);
                mutex.lock();
                fprintf(handle, "%s, %d\n", argv[1], j * i);
                mutex.unlock();
                sleep(countIter * j);
            }
        }
        else if(subPid < 0){
            KillChild(childPids);
            return 1;
        }
        else{
            childPids.push_back(subPid);
        }
    }

    int status = 0;
    if(subPid != 0){
        while (wait(&status) > 0) {
		    if (status != 0) {
				exit(1);
			}
		}
    }

    fclose(handle);
    return 0;
}
