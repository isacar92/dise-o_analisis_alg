#Código Cesar
def descifrar_cesar_bruto(mensaje):
    alfabeto = "abcdefghijklmnñopqrstuvwxyz ,."
    longitud = len(alfabeto)

    mapa_indices = {letra: pos for pos, letra in enumerate(alfabeto)}

    resultados_posibles = []

    for desplazamiento in range(longitud):
        texto_descifrado = ""

        for simbolo in mensaje:
            if simbolo in mapa_indices:
                nueva_pos = (mapa_indices[simbolo] - desplazamiento) % longitud
                texto_descifrado += alfabeto[nueva_pos]
            else:
                # Si no está en el alfabeto, se deja igual
                texto_descifrado += simbolo

        resultados_posibles.append((desplazamiento, texto_descifrado))

    return resultados_posibles


mensaje_cifrado = "l.ziu,mf .fzmk,wzilwgfqw mfai kwukmsw flw,wfifsif.upamz plilflmf .fik,.isfm k.lwfmufmsfk.isfmsfiñ.psiftmcpkiuifdfmsfkwulwzfiulpuwgfk.isfiamfjpkmnisigfxzw,mñmufmsflm xspmñ.mflmsftixiflmfitmzpkifsi,puigflm lmfsifnzwu,mzifuwz,mflmftmcpkwfoi ,ifmsfkijwflmfowzuw gfxsi tiulwfsif.upnpkikpwuflmfsw fpjmzwitmzpkiuw gfu.m ,zwfkwu,pumu,mfu.mawfdfiu,pñ.wgfxzmlm ,puilwfifkwu,mumzf.uifzieify.pu,igfsifzieifkw tpkigfmufsifk.isf mfn.ulpziufsi flp xmz i fdf mfkwu .tizifsif.uplilh"

intentos = descifrar_cesar_bruto(mensaje_cifrado)

for clave, posible in intentos:
    print(f"Clave {clave:2d}: {posible}\n")
