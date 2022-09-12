def interpret(command: str) -> str:
    return command.replace('(al)', 'al').replace('()', 'o')


print(interpret('G()(al)'))
# https://leetcode.com/problems/goal-parser-interpretation/
