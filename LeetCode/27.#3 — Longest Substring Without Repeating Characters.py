def func(s):

    max=0

    for i in range(len(s)):

        b=""

        for j in range(i,len(s)):

            if s[j] not in b:
                b=b+s[j]

                if len(b)>max:
                    max=len(b)

            else:
                break

    print(max)


s=input()

func(s)