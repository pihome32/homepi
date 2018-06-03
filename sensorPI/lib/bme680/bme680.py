from subprocess import check_output
test= check_output(["./readall", '1', '1'])
print(test)