from subprocess import Popen, PIPE
from colorPrint import printGreen,printYellow

filePath = 'Error samples\\{}.py'.format(input("Error name: "))      # script path/name that we want to test                                 
p = Popen(['python', filePath], stdout=PIPE, stderr=PIPE)            # Run the script in shell and retrieve stdout and stderr
output, error = p.communicate()                                      # Read output from the execution

# Check if the script failed to run and print the output and error messages
if p.returncode != 0: 
   printYellow("Execution Result: \n")
   
   printGreen("Return code:")
   print(p.returncode)
   
   printGreen("Output:")
   print(output.decode("utf-8"))
   
   printGreen("Error: ")
   print(error.decode("utf-8"))
    