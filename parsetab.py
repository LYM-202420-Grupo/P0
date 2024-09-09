
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN BALLOONSHERE CHIPSHERE COMMA DO DROP DROP_CHIP ELSE EXEC FI GOTO GRAB GRAB_BALLOON ID IF IS_BLOCKED IS_FACING JUMP LBRACE LET_GO LPAREN MOVE MOVES MYBALLOONS MYCHIPS MYX MYY NEW_MACRO NEW_VAR NOP NOT NUMBER OD PICK PICKUP_CHIP PLACE_BALLOON POP POP_BALLOON QUESTION RBRACE REP ROOMFORCHIPS RPAREN SAFE_EXE SEMICOLON SIZE THEN TIMES TURN_RIGHT TURN_TO_MY TURN_TO_THE WALK ZEROprogram : EXEC blockprogram : NEW_VAR ID ASSIGN NUMBERprogram : NEW_MACRO ID LPAREN param_list RPAREN blockblock : LBRACE stmt_list RBRACEstmt_list : stmt SEMICOLON stmt_list\n                 | stmt SEMICOLONstmt : IF condition THEN block ELSE block FI\n            | WALK LPAREN NUMBER RPAREN\n            | JUMP LPAREN NUMBER RPAREN\n            | DROP LPAREN NUMBER RPAREN\n            | MOVE LPAREN NUMBER RPAREN\n            | LET_GO LPAREN NUMBER RPAREN\n            | POP LPAREN NUMBER RPAREN\n            | TURN_TO_MY LPAREN ID RPAREN\n            | GRAB LPAREN ID RPAREN \n            | SAFE_EXE LPAREN stmt RPAREN\n            | MOVES LPAREN param_list RPAREN\n            | ID LPAREN param_list RPAREN\n            | REP NUMBER TIMES block\n            | NOP\n            | TURN_RIGHT LPAREN ID RPAREN\n            | TURN_TO_THE LPAREN ID RPAREN\n            | PICK LPAREN ID RPAREN\n            | GOTO LPAREN ID RPAREN\n            | DROP_CHIP LPAREN NUMBER RPAREN\n            | PLACE_BALLOON LPAREN NUMBER RPAREN\n            | GRAB_BALLOON LPAREN NUMBER RPAREN\n            | PICKUP_CHIP LPAREN NUMBER RPAREN\n            | POP_BALLOON LPAREN NUMBER RPARENstmt : DO block ODparam_list : ID COMMA param_list\n                  | ID\n                  | emptycondition : NOT LPAREN IS_BLOCKED LPAREN ID RPAREN RPAREN\n                 | NOT LPAREN ZERO QUESTION LPAREN ID RPAREN RPAREN\n                 | IS_BLOCKED LPAREN ID RPAREN\n                 | ZERO QUESTION LPAREN ID RPAREN\n                 | IS_FACING LPAREN ID RPAREN\n                 | SIZE\n                 | MYX\n                 | MYY \n                 | MYCHIPS\n                 | MYBALLOONS\n                 | BALLOONSHERE\n                 | CHIPSHERE\n                 | ROOMFORCHIPSempty :'
    
_lr_action_items = {'EXEC':([0,],[2,]),'NEW_VAR':([0,],[3,]),'NEW_MACRO':([0,],[4,]),'$end':([1,5,37,74,136,],[0,-1,-4,-2,-3,]),'LBRACE':([2,34,79,95,107,137,],[6,6,6,6,6,6,]),'ID':([3,4,6,36,38,58,59,60,61,62,64,65,66,67,81,83,106,112,138,145,],[7,8,19,75,19,90,75,92,19,75,96,97,98,99,111,113,75,141,144,149,]),'IF':([6,38,61,],[11,11,11,]),'WALK':([6,38,61,],[12,12,12,]),'JUMP':([6,38,61,],[13,13,13,]),'DROP':([6,38,61,],[14,14,14,]),'MOVE':([6,38,61,],[15,15,15,]),'LET_GO':([6,38,61,],[16,16,16,]),'POP':([6,38,61,],[17,17,17,]),'TURN_TO_MY':([6,38,61,],[18,18,18,]),'GRAB':([6,38,61,],[20,20,20,]),'SAFE_EXE':([6,38,61,],[21,21,21,]),'MOVES':([6,38,61,],[22,22,22,]),'REP':([6,38,61,],[23,23,23,]),'NOP':([6,38,61,],[24,24,24,]),'TURN_RIGHT':([6,38,61,],[25,25,25,]),'TURN_TO_THE':([6,38,61,],[26,26,26,]),'PICK':([6,38,61,],[27,27,27,]),'GOTO':([6,38,61,],[28,28,28,]),'DROP_CHIP':([6,38,61,],[29,29,29,]),'PLACE_BALLOON':([6,38,61,],[30,30,30,]),'GRAB_BALLOON':([6,38,61,],[31,31,31,]),'PICKUP_CHIP':([6,38,61,],[32,32,32,]),'POP_BALLOON':([6,38,61,],[33,33,33,]),'DO':([6,38,61,],[34,34,34,]),'ASSIGN':([7,],[35,]),'LPAREN':([8,12,13,14,15,16,17,18,19,20,21,22,25,26,27,28,29,30,31,32,33,40,41,43,82,109,139,],[36,52,53,54,55,56,57,58,59,60,61,62,64,65,66,67,68,69,70,71,72,80,81,83,112,138,145,]),'RBRACE':([9,38,78,],[37,-6,-5,]),'SEMICOLON':([10,24,37,105,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,147,],[38,-20,-4,-30,-8,-9,-10,-11,-12,-13,-14,-18,-15,-16,-17,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-7,]),'NOT':([11,],[40,]),'IS_BLOCKED':([11,80,],[41,109,]),'ZERO':([11,80,],[42,110,]),'IS_FACING':([11,],[43,]),'SIZE':([11,],[44,]),'MYX':([11,],[45,]),'MYY':([11,],[46,]),'MYCHIPS':([11,],[47,]),'MYBALLOONS':([11,],[48,]),'BALLOONSHERE':([11,],[49,]),'CHIPSHERE':([11,],[50,]),'ROOMFORCHIPS':([11,],[51,]),'NUMBER':([23,35,52,53,54,55,56,57,68,69,70,71,72,],[63,74,84,85,86,87,88,89,100,101,102,103,104,]),'RPAREN':([24,36,37,59,62,75,76,77,84,85,86,87,88,89,90,91,92,93,94,96,97,98,99,100,101,102,103,104,105,106,111,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,141,144,147,148,149,151,],[-20,-47,-4,-47,-47,-32,107,-33,114,115,116,117,118,119,120,121,122,123,124,126,127,128,129,130,131,132,133,134,-30,-47,140,142,-8,-9,-10,-11,-12,-13,-14,-18,-15,-16,-17,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-31,146,148,-7,150,151,152,]),'OD':([37,73,],[-4,105,]),'ELSE':([37,108,],[-4,137,]),'FI':([37,143,],[-4,147,]),'THEN':([39,44,45,46,47,48,49,50,51,140,142,146,150,152,],[79,-39,-40,-41,-42,-43,-44,-45,-46,-36,-38,-37,-34,-35,]),'QUESTION':([42,110,],[82,139,]),'TIMES':([63,],[95,]),'COMMA':([75,],[106,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'block':([2,34,79,95,107,137,],[5,73,108,125,136,143,]),'stmt_list':([6,38,],[9,78,]),'stmt':([6,38,61,],[10,10,93,]),'condition':([11,],[39,]),'param_list':([36,59,62,106,],[76,91,94,135,]),'empty':([36,59,62,106,],[77,77,77,77,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> EXEC block','program',2,'p_program_exec','analizador_lexico.py',82),
  ('program -> NEW_VAR ID ASSIGN NUMBER','program',4,'p_program_new_var','analizador_lexico.py',86),
  ('program -> NEW_MACRO ID LPAREN param_list RPAREN block','program',6,'p_program_new_macro','analizador_lexico.py',90),
  ('block -> LBRACE stmt_list RBRACE','block',3,'p_block','analizador_lexico.py',94),
  ('stmt_list -> stmt SEMICOLON stmt_list','stmt_list',3,'p_stmt_list','analizador_lexico.py',98),
  ('stmt_list -> stmt SEMICOLON','stmt_list',2,'p_stmt_list','analizador_lexico.py',99),
  ('stmt -> IF condition THEN block ELSE block FI','stmt',7,'p_stmt','analizador_lexico.py',103),
  ('stmt -> WALK LPAREN NUMBER RPAREN','stmt',4,'p_stmt','analizador_lexico.py',104),
  ('stmt -> JUMP LPAREN NUMBER RPAREN','stmt',4,'p_stmt','analizador_lexico.py',105),
  ('stmt -> DROP LPAREN NUMBER RPAREN','stmt',4,'p_stmt','analizador_lexico.py',106),
  ('stmt -> MOVE LPAREN NUMBER RPAREN','stmt',4,'p_stmt','analizador_lexico.py',107),
  ('stmt -> LET_GO LPAREN NUMBER RPAREN','stmt',4,'p_stmt','analizador_lexico.py',108),
  ('stmt -> POP LPAREN NUMBER RPAREN','stmt',4,'p_stmt','analizador_lexico.py',109),
  ('stmt -> TURN_TO_MY LPAREN ID RPAREN','stmt',4,'p_stmt','analizador_lexico.py',110),
  ('stmt -> GRAB LPAREN ID RPAREN','stmt',4,'p_stmt','analizador_lexico.py',111),
  ('stmt -> SAFE_EXE LPAREN stmt RPAREN','stmt',4,'p_stmt','analizador_lexico.py',112),
  ('stmt -> MOVES LPAREN param_list RPAREN','stmt',4,'p_stmt','analizador_lexico.py',113),
  ('stmt -> ID LPAREN param_list RPAREN','stmt',4,'p_stmt','analizador_lexico.py',114),
  ('stmt -> REP NUMBER TIMES block','stmt',4,'p_stmt','analizador_lexico.py',115),
  ('stmt -> NOP','stmt',1,'p_stmt','analizador_lexico.py',116),
  ('stmt -> TURN_RIGHT LPAREN ID RPAREN','stmt',4,'p_stmt','analizador_lexico.py',117),
  ('stmt -> TURN_TO_THE LPAREN ID RPAREN','stmt',4,'p_stmt','analizador_lexico.py',118),
  ('stmt -> PICK LPAREN ID RPAREN','stmt',4,'p_stmt','analizador_lexico.py',119),
  ('stmt -> GOTO LPAREN ID RPAREN','stmt',4,'p_stmt','analizador_lexico.py',120),
  ('stmt -> DROP_CHIP LPAREN NUMBER RPAREN','stmt',4,'p_stmt','analizador_lexico.py',121),
  ('stmt -> PLACE_BALLOON LPAREN NUMBER RPAREN','stmt',4,'p_stmt','analizador_lexico.py',122),
  ('stmt -> GRAB_BALLOON LPAREN NUMBER RPAREN','stmt',4,'p_stmt','analizador_lexico.py',123),
  ('stmt -> PICKUP_CHIP LPAREN NUMBER RPAREN','stmt',4,'p_stmt','analizador_lexico.py',124),
  ('stmt -> POP_BALLOON LPAREN NUMBER RPAREN','stmt',4,'p_stmt','analizador_lexico.py',125),
  ('stmt -> DO block OD','stmt',3,'p_stmt_do_while','analizador_lexico.py',129),
  ('param_list -> ID COMMA param_list','param_list',3,'p_param_list','analizador_lexico.py',133),
  ('param_list -> ID','param_list',1,'p_param_list','analizador_lexico.py',134),
  ('param_list -> empty','param_list',1,'p_param_list','analizador_lexico.py',135),
  ('condition -> NOT LPAREN IS_BLOCKED LPAREN ID RPAREN RPAREN','condition',7,'p_condition','analizador_lexico.py',139),
  ('condition -> NOT LPAREN ZERO QUESTION LPAREN ID RPAREN RPAREN','condition',8,'p_condition','analizador_lexico.py',140),
  ('condition -> IS_BLOCKED LPAREN ID RPAREN','condition',4,'p_condition','analizador_lexico.py',141),
  ('condition -> ZERO QUESTION LPAREN ID RPAREN','condition',5,'p_condition','analizador_lexico.py',142),
  ('condition -> IS_FACING LPAREN ID RPAREN','condition',4,'p_condition','analizador_lexico.py',143),
  ('condition -> SIZE','condition',1,'p_condition','analizador_lexico.py',144),
  ('condition -> MYX','condition',1,'p_condition','analizador_lexico.py',145),
  ('condition -> MYY','condition',1,'p_condition','analizador_lexico.py',146),
  ('condition -> MYCHIPS','condition',1,'p_condition','analizador_lexico.py',147),
  ('condition -> MYBALLOONS','condition',1,'p_condition','analizador_lexico.py',148),
  ('condition -> BALLOONSHERE','condition',1,'p_condition','analizador_lexico.py',149),
  ('condition -> CHIPSHERE','condition',1,'p_condition','analizador_lexico.py',150),
  ('condition -> ROOMFORCHIPS','condition',1,'p_condition','analizador_lexico.py',151),
  ('empty -> <empty>','empty',0,'p_empty','analizador_lexico.py',155),
]
