text = """
Insert text here.
"""
# Delete empty lines by replacing them with nothing.
step1 = text.replace("\n", "")
step2 = step1.replace(".", ". ")
step3 = step2.replace("!", "! ")
step4 = step3.replace(",", ", ")
step5 = step4.replace("?", "? ")
step6 = step5.replace("0:", "")
step7 = step6.replace("0", " ")
step8 = step7.replace("1:", " ")
step9 = step8.replace("1", " ")
step10 = step9.replace("2:", " ")
step11 = step10.replace("2", " ")
step12 = step11.replace("3:", " ")
step13 = step12.replace("3", " ")
step14 = step13.replace("4:", " ")
step15 = step14.replace("4", " ")
step16 = step15.replace("5:", " ")
step17 = step16.replace("5", " ")
step18 = step17.replace("6:", " ")
step19 = step18.replace("6", " ")
step20 = step19.replace("7:", " ")
step21 = step20.replace("7", " ")
step22 = step21.replace("8:", " ")
step23 = step22.replace("8", " ")
step24 = step23.replace("9:", " ")
step25 = step24.replace("9", " ")
step26 = step25.replace("0:", " ")
step27 = step26.replace("0", " ")
step28 = step27.replace("-->", "")
step29 = step28.replace("<i>", " ")
step30 = step29.replace("</i>", " ")
step31 = step30.replace("- ", "")
step32 = step31.replace("   ,", "")
step33 = step32.replace(":", ": ")
step34 = step33.replace(" …", "")
# Replace long dash with ordinary dash.
step35 = step34.replace("—", "– ")

# Delete all the spaces by turning the string into a list.
step36 = step35.split()
# Create a text made up of one paragraph using the join method.
step37 = " ".join(step36)

print(step37)
