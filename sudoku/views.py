from django.shortcuts import render, HttpResponse
import json
from . import sudoku
from .forms import SudokuForm

global FINAL, INITIAL, PUZZLE


def index(request, level=0):
    global FINAL, INITIAL, PUZZLE
    context = {}

    if request.method == 'POST':
        form = SudokuForm(request.POST)
        context['form'] = form
        form.is_valid()
        if check_solution(form.cleaned_data):
            context['WON'] = True
        else:
            context['WON'] = False
        print(context['WON'])

    else:
        FINAL, INITIAL, = get_initial_puzzle(level)
        PUZZLE = represent_puzzle_dict(INITIAL)
        form = SudokuForm()


    for i in PUZZLE:
        for j in i:
            form.fields[j['id']].initial = j['val']
            if j['val']:
                form.fields[j['id']].widget.attrs['readonly'] = True
                form.fields[j['id']].widget.attrs['style'] = 'background-color : #EEEEEE; '


    context['form'] = form
    context['level'] = get_level(level)
    try:
        context['WON']
    except:
        context['PLAYING'] = True
    return render(request, 'sudoku/home.html', context)


def get_level(level):
    if level == 0:
        return 'Very Easy'
    elif level == 1:
        return 'Easy'
    elif level == 2:
        return 'Medium'
    elif level == 3:
        return 'Hard'
    elif level == 4:
        return 'Evil'
    elif level == 5:
        return 'Impossible'



def check_solution(D):
    try:
        puzzle = [[0 for j in range(9)] for i in range(9)]
        for k, v in D.items():
            cell = ''
            for i in [s for s in k if s.isdigit()]:
                cell += i
            cell = int(cell)
            row = cell // 9
            col = cell - (row * 9)
            if v:
                puzzle[row][col] = int(v)
            else:
                puzzle[row][col] = 0
        print (puzzle)
        return sudoku.check_solution(puzzle)
    except:
        return False


def get_initial_puzzle(level=0):
    puzzle = sudoku.create_random_final_board()
    return puzzle, sudoku.create_initial_board(puzzle, level)

def represent_puzzle_dict(puzzle):
    result = []
    for row in range(len(puzzle)):
        row_dict = []
        for col in range(len(puzzle[row])):
            col_dict = {}
            if puzzle[row][col] == 0:
                col_dict['id'] = 'cell' + str(9*row + col)
                col_dict['val'] = ''
                col_dict['disabled'] = ''
            else:
                col_dict['val'] = (puzzle[row][col])
                col_dict['disabled'] = 'disabled'
                col_dict['id'] = 'cell' + str(9 * row + col)
            row_dict.append(col_dict)
        result.append(row_dict)
    return result
