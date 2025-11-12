def check_prefix(x: str, y: str):
    s_x=x.split()
    s_y=y.split()

    k=0

    for cuvant in s_y:
            for prefix in s_x:
                  if cuvant.startswith(prefix):
                        k=k+1
                        break
    return k

x="app app app"
y="apple application appetit appendicita"
print(check_prefix(x,y))