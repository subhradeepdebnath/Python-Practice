def func(k,s):

    if len(k)!=len(s):                 # pattern letters aur words ki length same honi chahiye

        print("false")
        return

    a={}                               # letter → word mapping
    b={}                               # word → letter mapping

    for i in range(len(k)):            # har letter aur word ko check karenge

        if k[i] in a:                  # agar letter pehle aa chuka hai

            if a[k[i]]!=s[i]:          # agar ab different word mil raha hai
                print("false")
                return

        else:

            a[k[i]]=s[i]               # letter ko word se map karo

        if s[i] in b:                  # agar word pehle aa chuka hai

            if b[s[i]]!=k[i]:          # agar word kisi aur letter se mapped hai
                print("false")
                return

        else:

            b[s[i]]=k[i]               # word ko letter se map karo

    print("true")


k=input()

s=input().split()

func(k,s)