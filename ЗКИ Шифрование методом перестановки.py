import PySimpleGUI as sg

layout = [	
			[sg.Text("Открытый текст: "), sg.InputText(key="-text-")],
			[sg.Output(size=(100, 25))],
			[sg.Button("Зашифровать")]]

window = sg.Window('ЭКИ "Шифрование методом перестановки"', layout)

while True:
	event, values = window.read()
	if event == "Зашифровать":

		if len(values["-text-"]) == 0:
			print("Ввод не должен пустовать.\n\n")
			continue

		text = "".join(values["-text-"].upper().split())

		i = 1
		while True:
			if i**2 >= len(text):
				break
			i+=1

		arrayI = 0
		openText = []
		for __ in range(i):
			openArray = []
			for ___ in range(i-1):
				try:
					openArray.append(text[arrayI])
				except:
					openArray.append(" ")
				arrayI+=1
			openText.append(openArray)

		print("Исходный текст")
		for __ in openText:
			print(" ".join(__))

		criptStroka = openText.copy()

		criptStroka.sort(key = lambda x: x[0])

		print("Шифрование по строке")
		for __ in criptStroka:
			print(" ".join(__))

		openTextMoved90 = []

		i = 0
		for __ in openText[0]:
			openArray = []
			for ___ in openText:
				openArray.append(___[i])
			openTextMoved90.append(openArray)
			i+=1

		openTextMoved90.sort(key = lambda x: x[0])

		openTextMoved90BackTo = []

		i = 0
		for __ in openTextMoved90[0]:
			openArray = []
			for ___ in openTextMoved90:
				openArray.append(___[i])
			openTextMoved90BackTo.append(openArray)
			i+=1

		print("Шифрование по столбцу")
		for __ in openTextMoved90BackTo:
			print(" ".join(__))

		print("Шифрование по строке и столбцу")
		openTextMoved90BackTo.sort(key = lambda x: x[0])

		for __ in openTextMoved90BackTo:
			print(" ".join(__))

		print("\n\n")

	elif event == None:
		sys.exit()