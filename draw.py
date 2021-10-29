class Draw:
    def __init__(self):
        self._step = 0
        self._drawings = {0: '|', 1: 'O', 2: '|', 3: '/', 4: '\\', 5: '/', 6: '\\'}
        self._drawing = [[[' '] for i in range(7)] for i in range(8)]
        for k in range(len(self._drawing[0])-2):
            self._drawing[0][k] = '_'
        for i in range(1, len(self._drawing)):
            self._drawing[i][0] = '|'

    def draw(self):
        if self._step in [0,1]:
            self._drawing[self._step + 1][len(self._drawing[0])-2] = self._drawings[self._step]
        if self._step ==2:
            self._drawing[self._step + 1][len(self._drawing[0]) - 2] = self._drawings[self._step]
            self._drawing[self._step + 2][len(self._drawing[0]) - 2] = self._drawings[self._step]


        if self._step in [5, 6]:
            self._drawing[3 + 2][len(self._drawing[0])-2 - 11 + 2*self._step] = self._drawings[self._step]
        if self._step in [3, 4]:
            self._drawing[2 + 1][len(self._drawing[0]) - 2 -7 +2*self._step] = self._drawings[self._step]
        self._step += 1

    def __str__(self):
        to_print = ''
        for i in range(len(self._drawing)):
            for j in self._drawing[i]:
                to_print += j[0] + ' '
            to_print += '\n'
        return to_print




if __name__ =='__main__' :
    a =  Draw()

    a.draw()
    a.draw()
    a.draw()
    a.draw()
    a.draw()
    a.draw()
    a.draw()
    print(a.drawing())

