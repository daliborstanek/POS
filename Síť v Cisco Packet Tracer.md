
## Popis

- Na PC1-4 jsem nastavil IP adresu 10.198.0.1-10.198.0.4
- Na obou switchích jsem nastavil pouze jméno S1 a S2 a uložil startup config
## Výpočet

- Součet ASCII hodnot: $83 + 84 + 65 + 78 + 69 + 75 = 454$
	
- **X** = $454 \pmod{256} = \mathbf{198}$
- Součet ASCII hodnot: $68 + 65 + 76 + 73 + 66 + 79 + 82 = 569$
    
- **Y** = $569 \pmod{10} = \mathbf{9}$
## Zde je nastavování S1

![[S1 nastavování.png]]

## Zde je ipconfig PC1 a pingování z PC1 na PC4

![[PC1 nastavování.png]]