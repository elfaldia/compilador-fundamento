
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DISTINTO DIVISION ID MULTIPLICACION NUMERO PARENTECISDER PARENTECISIZQ RESTA RESTO SUMA TNIRPstatement : ID DISTINTO expressionstatement : TNIRP PARENTECISDER expression PARENTECISIZQexpression : expression SUMA term\n                  | expression RESTA term\n                  | termterm : term MULTIPLICACION factor\n            | term DIVISION factor\n            | term RESTO factor\n            | factorfactor : NUMERO\n              | PARENTECISIZQ expression PARENTECISDER\n              | ID'
    
_lr_action_items = {'ID':([0,4,5,11,13,14,15,16,17,],[2,6,6,6,6,6,6,6,6,]),'TNIRP':([0,],[3,]),'$end':([1,6,7,8,9,10,19,20,21,22,23,24,25,],[0,-12,-1,-5,-9,-10,-2,-3,-4,-6,-7,-8,-11,]),'DISTINTO':([2,],[4,]),'PARENTECISDER':([3,6,8,9,10,18,20,21,22,23,24,25,],[5,-12,-5,-9,-10,25,-3,-4,-6,-7,-8,-11,]),'NUMERO':([4,5,11,13,14,15,16,17,],[10,10,10,10,10,10,10,10,]),'PARENTECISIZQ':([4,5,6,8,9,10,11,12,13,14,15,16,17,20,21,22,23,24,25,],[11,11,-12,-5,-9,-10,11,19,11,11,11,11,11,-3,-4,-6,-7,-8,-11,]),'MULTIPLICACION':([6,8,9,10,20,21,22,23,24,25,],[-12,15,-9,-10,15,15,-6,-7,-8,-11,]),'DIVISION':([6,8,9,10,20,21,22,23,24,25,],[-12,16,-9,-10,16,16,-6,-7,-8,-11,]),'RESTO':([6,8,9,10,20,21,22,23,24,25,],[-12,17,-9,-10,17,17,-6,-7,-8,-11,]),'SUMA':([6,7,8,9,10,12,18,20,21,22,23,24,25,],[-12,13,-5,-9,-10,13,13,-3,-4,-6,-7,-8,-11,]),'RESTA':([6,7,8,9,10,12,18,20,21,22,23,24,25,],[-12,14,-5,-9,-10,14,14,-3,-4,-6,-7,-8,-11,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([4,5,11,],[7,12,18,]),'term':([4,5,11,13,14,],[8,8,8,20,21,]),'factor':([4,5,11,13,14,15,16,17,],[9,9,9,9,9,22,23,24,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> ID DISTINTO expression','statement',3,'p_statement_assign','parser.py',9),
  ('statement -> TNIRP PARENTECISDER expression PARENTECISIZQ','statement',4,'p_statement_tnirp','parser.py',14),
  ('expression -> expression SUMA term','expression',3,'p_expression','parser.py',19),
  ('expression -> expression RESTA term','expression',3,'p_expression','parser.py',20),
  ('expression -> term','expression',1,'p_expression','parser.py',21),
  ('term -> term MULTIPLICACION factor','term',3,'p_term','parser.py',32),
  ('term -> term DIVISION factor','term',3,'p_term','parser.py',33),
  ('term -> term RESTO factor','term',3,'p_term','parser.py',34),
  ('term -> factor','term',1,'p_term','parser.py',35),
  ('factor -> NUMERO','factor',1,'p_factor','parser.py',48),
  ('factor -> PARENTECISIZQ expression PARENTECISDER','factor',3,'p_factor','parser.py',49),
  ('factor -> ID','factor',1,'p_factor','parser.py',50),
]
