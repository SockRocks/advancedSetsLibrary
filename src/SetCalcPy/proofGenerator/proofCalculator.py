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
        substitutions = {}
        complements = {}
        logical_statements = []

        paren_count = setExpression.count('(')
        for x in range(paren_count):
            cur_exp = ''
            ind = setExpression.find('(') + 1
            while setExpression[ind] != ')':
                cur_exp += setExpression[ind]
                ind += 1
            substitutions[f'#[{ind}]'] = cur_exp
            setExpression = setExpression[:ind-len(cur_exp) - 1] + f'#[{ind}]' + setExpression[ind + 1:]

        for x in range(setExpression.count('^c')):
            ind = setExpression.find('c')
            remaining = ''
            n_ind = ind - 2
            while setExpression[n_ind] != '+' and setExpression[n_ind] != '&' and setExpression[n_ind] != '*':
                if setExpression[n_ind] != '+' and setExpression[n_ind] != '&' and setExpression[n_ind] != '*':
                    remaining += setExpression[n_ind]
                n_ind -= 1
            remaining = remaining[::-1]
            complements[f'@[{ind}]'] = remaining
            setExpression = setExpression[:ind - len(remaining) - 1] + f'@[{ind}]' + setExpression[ind+1:]

        print(setExpression)
        if setExpression.startswith('x\in'):
            setExpression = setExpression[4:]
            print(setExpression)
            ind = 0
            for i in range(len(setExpression)):
                if i >= ind:
                    if i == 0:
                        cur_exp = ''
                        ind = 0
                        opp_count = 0
                        while opp_count < 2:
                            add = 1 if not self.checkEqualOperator(setExpression[ind]) or ind == len(setExpression) - 1 else 0
                            opp_count += add
                            if self.checkEqualOperator(setExpression[ind]) or opp_count <= 1:
                                cur_exp += setExpression[ind]
                            ind += 1
                        logical_statements.append(cur_exp)

                    else:
                        cur_exp = setExpression[i - 1]
                        ind = i
                        opp_count = 0
                        while opp_count < 1:
                            add = 1 if not self.checkEqualOperator(setExpression[ind]) or ind == len(setExpression) - 1 else 0
                            opp_count += add
                            if self.checkEqualOperator(setExpression[ind]):
                                cur_exp += setExpression[ind]
                            ind += 1
                        logical_statements.append(cur_exp)

            for i in range(len(logical_statements)):
                new = ''
                for y in logical_statements[i]:
                    if y != ' ':
                        new += y
                    logical_statements[i] = new

        print(logical_statements)


        return False

    def checkEqualOperator(self, statement):
        return statement != '+' and statement != '&' and statement != '*'

    def proveSubsetOf(self):
        LHS_logical = self.convertToLogical('x\in ' + self.LHS)
        #RHS_logical  = self.convertToLogical('x\in' + self.RHS)




def generateProof(statement):
    """
    Generates a proof of the submitted statement
    :param statement: A statement about sets (subset of equals)
    :return: A list to be printed as a proof of the statement
    """
    proofGen(statement)


generateProof('C+(A+B)^c<(A^c&B^c)+C')
#generateProof('C+B+D+K+U<D+B')