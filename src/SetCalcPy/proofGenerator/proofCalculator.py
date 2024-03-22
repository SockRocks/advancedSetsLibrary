class proofGen:
    RELATIONS = ('=', '<')

    def __init__(self, command):
        self.goal, self.LHS, self.RHS = self.parser(command)
        if self.goal == proofGen.RELATIONS[0]:
            self.proveEqual()
        elif self.goal == proofGen.RELATIONS[1]:
            self.proveSubsetOf()

    def parser(self, command):
        data = []
        count = 0
        goal = None
        for x in command:
            if x in proofGen.RELATIONS:
                count += 1
                goal = x
        if count > 1:
            pass
            # add too many goals error
        elif count < 1:
            pass
            # add too few goals error
        else:
            data.append(goal)
        LHS, RHS = command.split(goal)

        data.append(LHS)
        data.append(RHS)

        return data

    def convertToLogical(self, setExpression):
        

    def proveSubsetOf(self):





def generateProof(statement):
    """
    Generates a proof of the submitted statement
    :param statement: A statement about sets (subset of equals)
    :return: A list to be printed as a proof of the statement
    """
    proofGen(statement)