from subprocess import Popen, PIPE

# Prints text in colors
def prGreen(skk): print("\033[92m{}\033[00m" .format(skk), end='')            # Green
def prYellow(skk): print("\033[93m{}\033[00m" .format(skk), end='')          # Yellow

# script path/name that we want to test
filePath = 'Error samples\\{}.py'.format(input("Error name: "))                                        


p = Popen(['python', filePath], stdout=PIPE, stderr=PIPE)      # Run the script in shell and retrieve stdout and stderr
output, error = p.communicate()                                # Read output from the execution


# Check if the script failed to run and print the output and error messages
if p.returncode != 0: 
   prYellow("Execution Result: \n\n")
   
   prGreen("Return code:")
   print(p.returncode)
   
   prGreen("Output:")
   print(output)
   
   prGreen("Error: ")
   print(error)
    