import os
print(os.getenv("SESSION_SECRET"))
print(os.getenv("TEST_API_KEY_2"))
print(os.getenv("TEST_API_KEY_3"))

# Контейнер расчета


from sympy import *  # Что это означает? IT'S IMPORT BIBLYOTEK BRO | nice one 5/5
k, T, C, L = symbols('k T C L')

# 1 способ
C_ost = 40000
am_lst = []       
c_ost_lst = []   
years_method1 = 5

for i in range(years_method1):
    Am = (C - L) / T
    amortization = Am.subs({C: 40000, T: years_method1, L: 0})
    C_ost -= amortization
    am_lst.append(round(amortization, 2))
    c_ost_lst.append(round(C_ost, 2))

while len(am_lst) < 10:
    am_lst.append(0)
    c_ost_lst.append(c_ost_lst[-1] if c_ost_lst else 40000) 

print('am_lst (Linear):', am_lst)
print('c_ost_lst (Linear):', c_ost_lst)

# 2 способ
Aj = 0
C_ost = 40000
am_lst_2 = []
c_ost_lst_2 = []
period = 10 

for i in range(period):
    Am = k * 1/T * (C - Aj)
    amortization = Am.subs({C: 40000, T: period, k: 2})
    if C_ost <= 0:
        amortization = 0
    C_ost -= amortization
    if C_ost < 0:
        C_ost = 0
    am_lst_2.append(round(amortization, 2))
    Aj += amortization
    c_ost_lst_2.append(round(C_ost, 2))

print('am_lst_2 (Declining):', am_lst_2)
print('c_ost_lst_2 (Declining):', c_ost_lst_2)

# Табличный вывод

Y = range(1, 11) 

tbl1 = list(zip(Y, c_ost_lst, am_lst))
tbl2 = list(zip(Y, c_ost_lst_2, am_lst_2))

tframe = pd.DataFrame(tbl1, columns=['Y', 'c_ost', 'am'])
tframe2 = pd.DataFrame(tbl2, columns=['Y', 'c_ost_2', 'am_2'])

print("\n--- Table 1: Linear Amortization ---") # Что это означает? IT'S PRINT BRO | appreciate you 5/5
print(tframe)
print("\n--- Table 2: Declining Balance Amortization ---")
print(tframe2)

# Визуализация # Что это означает? IT'S IMPORT BIBLYOTEK BRO | okay okay 4/5

fig, axes = plt.subplots(1, 3, figsize=(18, 6))

axes[0].plot(tframe['Y'], tframe['c_ost'], label='Linear (5-yr)', color='blue', marker='o', linewidth=2)
axes[0].plot(tframe2['Y'], tframe2['c_ost_2'], label='Declining (10-yr)', color='red', marker='s', linewidth=2)
axes[0].set_title('Remaining Asset Value Over 10 Years')
axes[0].set_xlabel('Year')
axes[0].set_ylabel('Remaining Cost')
axes[0].legend()
axes[0].grid(True, alpha=0.3)
axes[0].set_xticks(range(1, 11))

# Subplot 1
axes[1].pie(am_lst,
            labels=range(1, period + 1),
            explode=[0.1] * period,
            autopct=lambda pct: f'{pct:.1f}%' if pct > 0 else '',
            shadow=True,
            wedgeprops={
                'edgecolor': 'k',
                'lw': 1,
                'ls': '--'
            },
            rotatelabels=True)
axes[1].set_title('Amortization % (Linear, 5-yr over 10)')
axes[1].axis('equal')

# Subplot 2
axes[2].pie(am_lst_2,
            labels=range(1, period + 1),
            explode=[0.1] * period,
            autopct=lambda pct: f'{pct:.1f}%' if pct > 0 else '',
            shadow=True,
            wedgeprops={
                'edgecolor': 'k',
                'lw': 1,
                'ls': '--'
            },
            rotatelabels=True)
axes[2].set_title('Amortization % (Declining, 10-yr)')
axes[2].axis('equal')

plt.tight_layout()
plt.show()

