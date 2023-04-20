from glob import glob
import re

def main():
    logs = glob('./logs/*.log')
    # reg_ip = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    reg_ip = r"^(.+?)\s"
    
    for log_file_name in logs:
        with open(log_file_name) as f:
            lines = [line.strip() for line in f]
            for line in lines:
                result =re.findall(reg_ip,line) 
                print(result)


if __name__=='__main__':
    main()
