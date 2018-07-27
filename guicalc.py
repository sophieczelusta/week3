import wx
from math import sqrt

def binary(bi): #binary to base ten
    if "2" in bi or "3" in bi or "4" in bi or "5" in bi or "6" in bi or "7" in bi or "8" in bi or "9" in bi:
        return "Binary must consist of ones and zeroes."
    else:
        answer2 = 0
        if "." not in bi:
            length = len(bi)
            count = 0
            answer = 0
            newl = length - 1
            for number in range(length):
                result = int(bi[newl]) * (2 ** count)
                result = float(result)
                answer = result + answer
                count += 1
                newl -= 1
            return answer
        else:
            start = bi[0:bi.index(".")]
            end = bi = bi[bi.index("."):len(bi)]
            length = len(start)
            length2 = len(end)
            count = 0
            count2 = 1
            answer = 0
            answer2 = 0
            newl = length - 1
            newl2 = length2 - 1
            for number in range(length):
                result = int(start[newl]) * (2 ** count)
                result = float(result)
                answer = result + answer
                count += 1
                newl -= 1
            for number in range(length2):
                result2 = int(start[newl2]) * (2 ** -count2)
                result2 = float(result2)
                answer2 = result2 + answer2
                count2 += 1
                newl2 -= 1
            result = answer + answer2
            return result

def octal(number): #binary to octal
    if "." in number:
        [predec,postdec] = number.split(".")
    else:
        predec = number
        postdec = "0"
    count = 0
    count2 = 0
    side_a = len(predec)
    side_b = len(postdec)
    output = ""
    if side_a % 3 == 1:
        predec = "00" + predec
    elif side_a % 3 == 2:
        predec = "0" + predec
    else:
        predec = predec
    while count < len(predec):
        current = predec[count:count + 3]
        if current == "000":
            output = output + "0"
        elif current == "001":
            output = output + "1"
        elif current == "010":
            output = output + "2"
        elif current == "011":
            output = output + "3"
        elif current == "100":
            output = output + "4"
        elif current == "101":
            output = output + "5"
        elif current == "110":
            output = output + "6"
        elif current == "111":
            output = output + "7"
        else:
            return "Binary must consist of ones and zeroes."
        count = count + 3
        if count >= len(predec):
            break
    output = output + "."
    if side_b % 3 == 1:
        postdec = postdec + "00"
    elif side_b % 3 == 2:
        postdec = postdec + "0"
    else:
        postdec = postdec
    while count2 < len(postdec):
        current = postdec[count2:count2 + 3]
        if current == "000":
            output = output + "0"
        elif current == "001":
            output = output + "1"
        elif current == "010":
            output = output + "2"
        elif current == "011":
            output = output + "3"
        elif current == "100":
            output = output + "4"
        elif current == "101":
            output = output + "5"
        elif current == "110":
            output = output + "6"
        elif current == "111":
            output = output + "7"
        else:
            return "Binary must consist of ones and zeroes."
        count2 = count2 + 3
        if count2 >= len(postdec):
            break
    return output

def hexa(binary):
    if "." in binary:
        [predec,postdec] = binary.split(".")
    else:
        predec = binary
        postdec = "0"
    count = 0
    count2 = 0
    side_a = len(predec)
    side_b = len(postdec)
    output = ""
    if side_a % 4 == 1:
        predec = "000" + predec
    elif side_a % 4 == 2:
        predec = "00" + predec
    elif side_a % 4 == 3:
        predec = "0" + predec
    else:
        predec = predec
    if side_b % 4 == 1:
        postdec = postdec + "000"
    elif side_b % 4 == 2:
        postdec = postdec + "00"
    elif side_b % 4 == 3:
        postdec = "0" + postdec
    else:
        postdec = postdec
    while count < len(predec):
        current = predec[count:count + 4]
        if current == "0000":
            output = output + "0"
        elif current == "0001":
            output = output + "1"
        elif current == "0010":
            output = output + "2"
        elif current == "0011":
            output = output + "3"
        elif current == "0100":
            output = output + "4"
        elif current == "0101":
            output = output + "5"
        elif current == "0110":
            output = output + "6"
        elif current == "0111":
            output = output + "7"
        elif current == "1000":
            output = output + "8"
        elif current == "1001":
            output = output + "9"
        elif current == "1010":
            output = output + "A"
        elif current == "1011":
            output = output + "B"
        elif current == "1100":
            output = output + "C"
        elif current == "1101":
            output = output + "D"
        elif current == "1110":
            output = output + "E"
        elif current == "1111":
            output = output + "F"
        else:
            return "Binary must consist of ones and zeroes."
        count += 4
    output = output + "."
    while count2 < len(postdec):
        current = postdec[count2:count2 + 4]
        if current == "0000":
            output = output + "0"
        elif current == "0001":
            output = output + "1"
        elif current == "0010":
            output = output + "2"
        elif current == "0011":
            output = output + "3"
        elif current == "0100":
            output = output + "4"
        elif current == "0101":
            output = output + "5"
        elif current == "0110":
            output = output + "6"
        elif current == "0111":
            output = output + "7"
        elif current == "1000":
            output = output + "8"
        elif current == "1001":
            output = output + "9"
        elif current == "1010":
            output = output + "A"
        elif current == "1011":
            output = output + "B"
        elif current == "1100":
            output = output + "C"
        elif current == "1101":
            output = output + "D"
        elif current == "1110":
            output = output + "E"
        elif current == "1111":
            output = output + "F"
        else:
            return "Binary must consist of ones and zeroes."
        count2 += 4
    return output

def baseten(base):#baseten-binary
    final = ""
    if "." not in base:
        result = bin(int(base))
        if "0b" in str(result):
            result = result[2:]
        else:
            result = result
        return result
    else:
        counter = .5
        dig = 0
        saved = 0
        [predec,postdec] = base.split(".")
        result = bin(int(predec))
        result = str(result[2:])
        while float(postdec) >= 2:
            remainder = float(postdec) % 2
            final = final + str(remainder)
            postdec = float(postdec) // 2
            if postdec < 2:
                final = final + "1"
        result = result + "." + final
        return result






class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,
        size=(400,300))

        self.InitUI()
        self.Centre()


    def InitUI(self):

    #    menubar = wx.MenuBar()
    #    fileMenu = wx.Menu()
    #    menubar.Append(fileMenu, '&File')
    #    self.SetMenuBar(menubar)

        vbox = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(self, style=wx.TE_RIGHT)
        vbox.Add(self.display, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=4)
        gs = wx.GridSizer(6,4,6,6)

        buttons = [
            '√','**','CLEAR','CLEAR ALL',
            '7','8','9','/',
            '4','5','6','*',
            '1','2','3','-',
            '0','.','=','+',
            'Bi-Base10','Bi-Octal','Bi-Hexadec'
        ]

        for label in buttons:
            button = wx.Button(self,-1,label)
            gs.Add(button,0,wx.EXPAND)
            self.Bind(wx.EVT_BUTTON, self.on_button_press, button)

        vbox.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)

    def on_button_press(self,e):
        label = e.GetEventObject().GetLabel()
        calculation = self.display.GetValue()
        if label == "=":
            if not calculation:
                return
            result = eval(calculation)
            self.display.SetValue(str(result))
        elif label == "CLEAR ALL":
            self.display.SetValue('')
        elif label == "√":
            if calculation[0] == '-':
                self.display.SetValue('Cannot determine square root of negative.')
            else:
                result = sqrt(float(calculation))
                result = str(result)
                self.display.SetValue(result)
        elif label == "CLEAR":
            length = len(calculation)
            if length <= 0:
                return
            else:
                calculation = list(calculation)
                calculation.remove(calculation[length - 1])
                calculation = "".join(calculation)
                self.display.SetValue(calculation)
        elif label == "Bi-Base10":
            self.display.SetValue(str(binary(calculation)))
        elif label == "Bi-Octal":
            self.display.SetValue(str(octal(calculation)))
        elif label == "Bi-Hexadec":
            self.display.SetValue(str(hexa(calculation)))
        elif label == "Base10-Bi":
            self.display.SetValue(str(baseten(calculation)))
        else:
            self.display.SetValue(calculation + label)

def main():

    app = wx.App()
    ex = Example(None, title='Calculator')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
