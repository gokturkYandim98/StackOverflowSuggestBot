from subprocess import Popen, PIPE

# script path/name that we want to test
filePath = 'Sample Error Codes'
scriptName = '\\test1.py'                                        

p = Popen(['python', filePath + scriptName], stdout=PIPE, stderr=PIPE)    # Run the script in shell and retrieve stdout and stderr
output, error = p.communicate()                                # Read output from the execution

# Check if the script was failed to run and print the output and error messages
if p.returncode != 0: 
   print("Return code: %d " % (p.returncode))
   print("Output:  %s" % (output))
   print("Error: %s" % (error))
    