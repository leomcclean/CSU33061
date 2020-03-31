fit                     = 0
unfit                   = 1
dead                    = 2
exercise                = 1
relax                   = 0

exerciseReward          = [[8,8,0],[0,0,0],[0,0,0]]
relaxReward             = [[10,10,0],[5,5,0],[0,0,0]]
exerciseProbability     = [[.891,.009,.01],[.18,.72,.1],[0,0,1]]
relaxProbability        = [[.693,.297,.01],[0,.99,.01],[0,0,1]]

γ                       = 0

def main():
    global γ

    while True:
        print("enter n: ")
        n = int(input())
        if n < 0:
            print("n must be a positive integer.")
        else:
            break
    while True:
        print("enter γ: ")
        γ = float(input())
        if γ > 1 or γ < 0:
            print("γ must be between 0 and 1.")
        else:
            break
    while True:
        print("enter state: ")
        state = int(input())
        if state != fit and state != unfit and state != dead:
            print(fit)
            print("state must be 0 (fit), 1 (unfit), or 2 (dead).")
        else:
            break

    for i in range(0,n+1):
        print("exercise: " + str(q(state,exercise,i)) + ", relax: " + str(q(state,relax,i)))
    return

def q(s, a, state):
    pFit    = p(s,a,fit)
    pUnfit  = p(s,a,unfit)
    q0      = pFit * r(s,a,fit) + pUnfit * r(s,a,unfit)
    if state is fit:
        return q0
    else:
        return q0 + γ * (pFit * v(fit,state-1) + pUnfit * v(unfit,state-1))

def p(s, a, state):
    if a == exercise:
        return exerciseProbability[s][state]
    else:
        return relaxProbability[s][state]

def r(s, a, state):
    if a == exercise:
        return exerciseReward[s][state]
    else:
        return relaxReward[s][state]

def v(s1,s2):
    return max(q(s1,exercise,s2),q(s1,relax,s2))

if __name__ == "__main__":
    main()