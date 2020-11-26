
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftELSEIFleftELSEleftORleftANDleftNOTleftGTLTNEEQLEGEleftMODleftSUMSUBleftMULDIVleftINTEGERNUMBERleftFLOATNUMBERleftTRUEFALSEleftIDrightASSIGNleftERRORAND ASSIGN BOOLEAN COLON COMMA DIV ELSE ELSEIF EQ ERROR FALSE FLOAT FLOATNUMBER FOR FUNCTION GE GT ID IF IN INTEGER INTEGERNUMBER LCB LE LRB LSB LT MAIN MOD MUL NE NOT ON OR PRINT RCB RETURN RRB RSB SEMICOLON SUB SUM TRUE WHERE WHILEprogram : declist MAIN LRB RRB block\n                    | MAIN LRB RRB blockdeclist : dec\n                   | declist decdec : vardec\n               | funcdectype : INTEGER\n                | FLOAT\n                | BOOLEANiddec : ID\n                 | ID LSB exp RSB\n                 | ID ASSIGN expidlist : iddec\n                  | idlist COMMA iddecvardec : idlist COLON type SEMICOLONfuncdec : FUNCTION ID LRB paramdecs RRB COLON type block\n                   | FUNCTION ID LRB paramdecs RRB blockparamdecs : paramdecslist\n                     | emptyparamdecslist : paramdec\n                         | paramdecslist COMMA paramdec paramdec : ID COLON type\n                     | ID LSB RSB COLON typeblock : LCB stmtlist RCBstmtlist : stmtlist stmt\n                    | emptylvalue : ID\n                  | ID LSB exp RSBcase : WHERE const COLON stmtlistcases : cases case\n                | emptystmt : RETURN exp SEMICOLON\n                | exp SEMICOLON\n                | block\n                | vardec\n                | WHILE LRB exp RRB stmt\n                | ON LRB exp RRB LCB cases RCB SEMICOLON\n                | FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt\n                | FOR LRB ID IN ID RRB stmt\n                | IF LRB exp RRB stmt elseiflist\n                | IF LRB exp RRB stmt elseiflist ELSE stmt\n                | PRINT LRB ID RRB SEMICOLONelseiflist : elseiflist ELSEIF LRB exp RRB stmt\n                      | emptyexp : lvalue ASSIGN exp\n               | exp GT exp\n               | exp LT exp\n               | exp NE exp\n               | exp EQ exp\n               | exp LE exp\n               | exp GE exp\n               | exp AND exp\n               | exp OR exp\n               | exp SUM exp\n               | exp SUB exp\n               | exp MUL exp\n               | exp DIV exp\n               | exp MOD exp\n               | const\n               | lvalue\n               | ID LRB explist RRB\n               | LRB exp RRB\n               | ID LRB RRB\n               | SUB exp\n               | NOT expconst : INTEGERNUMBER\n                 | FLOATNUMBER\n                 | TRUE\n                 | FALSEexplist : exp\n                   | explist COMMA expempty :'
    
_lr_action_items = {'MAIN':([0,2,4,5,6,12,42,94,109,134,],[3,11,-3,-5,-6,-4,-15,-24,-17,-16,]),'FUNCTION':([0,2,4,5,6,12,42,94,109,134,],[8,8,-3,-5,-6,-4,-15,-24,-17,-16,]),'ID':([0,2,4,5,6,8,12,15,17,18,26,30,32,33,41,42,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,69,70,74,94,95,96,98,99,109,112,115,116,117,118,119,120,121,125,134,135,137,138,140,142,146,147,150,151,152,153,158,159,161,163,164,165,166,167,169,170,171,],[9,9,-3,-5,-6,16,-4,9,27,27,43,27,27,27,-72,-15,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,103,-26,43,-24,-25,27,-34,-35,-17,27,-33,27,27,129,27,27,132,-32,-16,103,27,145,103,-36,-72,-42,27,103,-40,-44,-39,103,-37,103,-41,27,-72,-38,103,103,-43,]),'$end':([1,40,68,94,],[0,-2,-1,-24,]),'LRB':([3,11,16,17,18,27,30,32,33,41,42,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,69,70,94,95,96,98,99,100,101,102,103,104,105,112,115,116,117,118,119,120,125,129,135,137,140,142,146,147,150,151,152,153,158,159,160,161,163,164,165,166,167,169,170,171,],[13,19,26,32,32,48,32,32,32,-72,-15,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-26,-24,-25,32,-34,-35,116,117,118,48,120,121,32,-33,32,32,32,32,32,-32,48,32,32,32,-36,-72,-42,32,32,-40,-44,-39,32,165,-37,32,-41,32,-72,-38,32,32,-43,]),'COLON':([7,9,10,25,27,29,31,34,35,36,37,38,43,50,65,67,73,76,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,103,107,111,113,139,162,],[14,-10,-13,-14,-27,-60,-59,-66,-67,-68,-69,-12,71,-11,-64,-65,108,-63,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-45,-62,-10,122,-61,-28,-11,166,]),'COMMA':([7,9,10,22,23,24,25,27,29,31,34,35,36,37,38,45,47,50,65,67,75,76,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,103,106,110,111,113,124,133,139,],[15,-10,-13,-7,-8,-9,-14,-27,-60,-59,-66,-67,-68,-69,-12,74,-20,-11,-64,-65,112,-63,-70,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-45,-62,-10,-22,-21,-61,-28,-71,-23,-11,]),'LSB':([9,27,43,103,129,],[17,49,72,119,49,]),'ASSIGN':([9,27,29,103,113,129,139,],[18,-27,64,18,-28,-27,-28,]),'RRB':([13,19,22,23,24,26,27,29,31,34,35,36,37,44,45,46,47,48,65,66,67,75,76,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,106,110,111,113,124,126,127,131,132,133,145,157,168,],[20,39,-7,-8,-9,-72,-27,-60,-59,-66,-67,-68,-69,73,-18,-19,-20,76,-64,93,-65,111,-63,-70,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-45,-62,-22,-21,-61,-28,-71,135,136,140,141,-23,151,163,170,]),'INTEGER':([14,71,108,122,],[22,22,22,22,]),'FLOAT':([14,71,108,122,],[23,23,23,23,]),'BOOLEAN':([14,71,108,122,],[24,24,24,24,]),'SUB':([17,18,27,28,29,30,31,32,33,34,35,36,37,38,41,42,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,70,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,103,111,112,113,114,115,116,117,118,119,120,124,125,126,127,128,129,130,131,135,137,139,140,142,144,146,147,150,151,152,153,157,158,159,161,163,164,165,166,167,168,169,170,171,],[30,30,-27,60,-60,30,-59,30,30,-66,-67,-68,-69,60,-72,-15,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,-64,60,60,30,-26,-63,60,60,60,60,60,60,60,60,60,60,-54,-55,-56,-57,60,-45,-62,-24,-25,30,60,-34,-35,-27,-61,30,-28,60,-33,30,30,30,30,30,60,-32,60,60,60,-27,60,60,30,30,-28,30,-36,60,-72,-42,30,30,-40,-44,60,-39,30,-37,30,-41,30,-72,-38,60,30,30,-43,]),'NOT':([17,18,30,32,33,41,42,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,69,70,94,95,96,98,99,112,115,116,117,118,119,120,125,135,137,140,142,146,147,150,151,152,153,158,159,161,163,164,165,166,167,169,170,171,],[33,33,33,33,33,-72,-15,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,-26,-24,-25,33,-34,-35,33,-33,33,33,33,33,33,-32,33,33,33,-36,-72,-42,33,33,-40,-44,-39,33,-37,33,-41,33,-72,-38,33,33,-43,]),'INTEGERNUMBER':([17,18,30,32,33,41,42,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,69,70,94,95,96,98,99,112,115,116,117,118,119,120,125,135,137,140,142,146,147,150,151,152,153,156,158,159,161,163,164,165,166,167,169,170,171,],[34,34,34,34,34,-72,-15,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,-26,-24,-25,34,-34,-35,34,-33,34,34,34,34,34,-32,34,34,34,-36,-72,-42,34,34,-40,-44,34,-39,34,-37,34,-41,34,-72,-38,34,34,-43,]),'FLOATNUMBER':([17,18,30,32,33,41,42,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,69,70,94,95,96,98,99,112,115,116,117,118,119,120,125,135,137,140,142,146,147,150,151,152,153,156,158,159,161,163,164,165,166,167,169,170,171,],[35,35,35,35,35,-72,-15,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,-26,-24,-25,35,-34,-35,35,-33,35,35,35,35,35,-32,35,35,35,-36,-72,-42,35,35,-40,-44,35,-39,35,-37,35,-41,35,-72,-38,35,35,-43,]),'TRUE':([17,18,30,32,33,41,42,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,69,70,94,95,96,98,99,112,115,116,117,118,119,120,125,135,137,140,142,146,147,150,151,152,153,156,158,159,161,163,164,165,166,167,169,170,171,],[36,36,36,36,36,-72,-15,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-26,-24,-25,36,-34,-35,36,-33,36,36,36,36,36,-32,36,36,36,-36,-72,-42,36,36,-40,-44,36,-39,36,-37,36,-41,36,-72,-38,36,36,-43,]),'FALSE':([17,18,30,32,33,41,42,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,69,70,94,95,96,98,99,112,115,116,117,118,119,120,125,135,137,140,142,146,147,150,151,152,153,156,158,159,161,163,164,165,166,167,169,170,171,],[37,37,37,37,37,-72,-15,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,-26,-24,-25,37,-34,-35,37,-33,37,37,37,37,37,-32,37,37,37,-36,-72,-42,37,37,-40,-44,37,-39,37,-37,37,-41,37,-72,-38,37,37,-43,]),'LCB':([20,22,23,24,39,41,42,69,70,73,94,95,98,99,115,123,125,135,136,140,142,146,147,151,152,153,158,159,161,163,164,166,167,169,170,171,],[41,-7,-8,-9,41,-72,-15,41,-26,41,-24,-25,-34,-35,-33,41,-32,41,143,41,-36,-72,-42,41,-40,-44,-39,41,-37,41,-41,-72,-38,41,41,-43,]),'SEMICOLON':([21,22,23,24,27,29,31,34,35,36,37,65,67,76,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,97,103,111,113,114,128,129,139,141,144,154,],[42,-7,-8,-9,-27,-60,-59,-66,-67,-68,-69,-64,-65,-63,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-45,-62,115,-27,-61,-28,125,137,-27,-28,147,150,161,]),'RSB':([27,28,29,31,34,35,36,37,65,67,72,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,111,113,130,],[-27,50,-60,-59,-66,-67,-68,-69,-64,-65,107,-63,113,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-45,-62,-61,-28,139,]),'GT':([27,28,29,31,34,35,36,37,38,65,66,67,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,97,103,111,113,114,124,126,127,128,129,130,131,139,144,157,168,],[-27,51,-60,-59,-66,-67,-68,-69,51,-64,51,51,-63,51,51,-46,-47,-48,-49,-50,-51,51,51,-54,-55,-56,-57,-58,-45,-62,51,-27,-61,-28,51,51,51,51,51,-27,51,51,-28,51,51,51,]),'LT':([27,28,29,31,34,35,36,37,38,65,66,67,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,97,103,111,113,114,124,126,127,128,129,130,131,139,144,157,168,],[-27,52,-60,-59,-66,-67,-68,-69,52,-64,52,52,-63,52,52,-46,-47,-48,-49,-50,-51,52,52,-54,-55,-56,-57,-58,-45,-62,52,-27,-61,-28,52,52,52,52,52,-27,52,52,-28,52,52,52,]),'NE':([27,28,29,31,34,35,36,37,38,65,66,67,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,97,103,111,113,114,124,126,127,128,129,130,131,139,144,157,168,],[-27,53,-60,-59,-66,-67,-68,-69,53,-64,53,53,-63,53,53,-46,-47,-48,-49,-50,-51,53,53,-54,-55,-56,-57,-58,-45,-62,53,-27,-61,-28,53,53,53,53,53,-27,53,53,-28,53,53,53,]),'EQ':([27,28,29,31,34,35,36,37,38,65,66,67,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,97,103,111,113,114,124,126,127,128,129,130,131,139,144,157,168,],[-27,54,-60,-59,-66,-67,-68,-69,54,-64,54,54,-63,54,54,-46,-47,-48,-49,-50,-51,54,54,-54,-55,-56,-57,-58,-45,-62,54,-27,-61,-28,54,54,54,54,54,-27,54,54,-28,54,54,54,]),'LE':([27,28,29,31,34,35,36,37,38,65,66,67,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,97,103,111,113,114,124,126,127,128,129,130,131,139,144,157,168,],[-27,55,-60,-59,-66,-67,-68,-69,55,-64,55,55,-63,55,55,-46,-47,-48,-49,-50,-51,55,55,-54,-55,-56,-57,-58,-45,-62,55,-27,-61,-28,55,55,55,55,55,-27,55,55,-28,55,55,55,]),'GE':([27,28,29,31,34,35,36,37,38,65,66,67,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,97,103,111,113,114,124,126,127,128,129,130,131,139,144,157,168,],[-27,56,-60,-59,-66,-67,-68,-69,56,-64,56,56,-63,56,56,-46,-47,-48,-49,-50,-51,56,56,-54,-55,-56,-57,-58,-45,-62,56,-27,-61,-28,56,56,56,56,56,-27,56,56,-28,56,56,56,]),'AND':([27,28,29,31,34,35,36,37,38,65,66,67,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,97,103,111,113,114,124,126,127,128,129,130,131,139,144,157,168,],[-27,57,-60,-59,-66,-67,-68,-69,57,-64,57,-65,-63,57,57,-46,-47,-48,-49,-50,-51,-52,57,-54,-55,-56,-57,-58,-45,-62,57,-27,-61,-28,57,57,57,57,57,-27,57,57,-28,57,57,57,]),'OR':([27,28,29,31,34,35,36,37,38,65,66,67,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,97,103,111,113,114,124,126,127,128,129,130,131,139,144,157,168,],[-27,58,-60,-59,-66,-67,-68,-69,58,-64,58,-65,-63,58,58,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-45,-62,58,-27,-61,-28,58,58,58,58,58,-27,58,58,-28,58,58,58,]),'SUM':([27,28,29,31,34,35,36,37,38,65,66,67,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,97,103,111,113,114,124,126,127,128,129,130,131,139,144,157,168,],[-27,59,-60,-59,-66,-67,-68,-69,59,-64,59,59,-63,59,59,59,59,59,59,59,59,59,59,-54,-55,-56,-57,59,-45,-62,59,-27,-61,-28,59,59,59,59,59,-27,59,59,-28,59,59,59,]),'MUL':([27,28,29,31,34,35,36,37,38,65,66,67,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,97,103,111,113,114,124,126,127,128,129,130,131,139,144,157,168,],[-27,61,-60,-59,-66,-67,-68,-69,61,61,61,61,-63,61,61,61,61,61,61,61,61,61,61,61,61,-56,-57,61,-45,-62,61,-27,-61,-28,61,61,61,61,61,-27,61,61,-28,61,61,61,]),'DIV':([27,28,29,31,34,35,36,37,38,65,66,67,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,97,103,111,113,114,124,126,127,128,129,130,131,139,144,157,168,],[-27,62,-60,-59,-66,-67,-68,-69,62,62,62,62,-63,62,62,62,62,62,62,62,62,62,62,62,62,-56,-57,62,-45,-62,62,-27,-61,-28,62,62,62,62,62,-27,62,62,-28,62,62,62,]),'MOD':([27,28,29,31,34,35,36,37,38,65,66,67,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,97,103,111,113,114,124,126,127,128,129,130,131,139,144,157,168,],[-27,63,-60,-59,-66,-67,-68,-69,63,-64,63,63,-63,63,63,63,63,63,63,63,63,63,63,-54,-55,-56,-57,-58,-45,-62,63,-27,-61,-28,63,63,63,63,63,-27,63,63,-28,63,63,63,]),'RCB':([41,42,69,70,94,95,98,99,115,125,142,143,146,147,148,149,152,153,155,158,161,164,166,167,169,171,],[-72,-15,94,-26,-24,-25,-34,-35,-33,-32,-36,-72,-72,-42,154,-31,-40,-44,-30,-39,-37,-41,-72,-38,-29,-43,]),'RETURN':([41,42,69,70,94,95,98,99,115,125,135,140,142,146,147,151,152,153,158,159,161,163,164,166,167,169,170,171,],[-72,-15,96,-26,-24,-25,-34,-35,-33,-32,96,96,-36,-72,-42,96,-40,-44,-39,96,-37,96,-41,-72,-38,96,96,-43,]),'WHILE':([41,42,69,70,94,95,98,99,115,125,135,140,142,146,147,151,152,153,158,159,161,163,164,166,167,169,170,171,],[-72,-15,100,-26,-24,-25,-34,-35,-33,-32,100,100,-36,-72,-42,100,-40,-44,-39,100,-37,100,-41,-72,-38,100,100,-43,]),'ON':([41,42,69,70,94,95,98,99,115,125,135,140,142,146,147,151,152,153,158,159,161,163,164,166,167,169,170,171,],[-72,-15,101,-26,-24,-25,-34,-35,-33,-32,101,101,-36,-72,-42,101,-40,-44,-39,101,-37,101,-41,-72,-38,101,101,-43,]),'FOR':([41,42,69,70,94,95,98,99,115,125,135,140,142,146,147,151,152,153,158,159,161,163,164,166,167,169,170,171,],[-72,-15,102,-26,-24,-25,-34,-35,-33,-32,102,102,-36,-72,-42,102,-40,-44,-39,102,-37,102,-41,-72,-38,102,102,-43,]),'IF':([41,42,69,70,94,95,98,99,115,125,135,140,142,146,147,151,152,153,158,159,161,163,164,166,167,169,170,171,],[-72,-15,104,-26,-24,-25,-34,-35,-33,-32,104,104,-36,-72,-42,104,-40,-44,-39,104,-37,104,-41,-72,-38,104,104,-43,]),'PRINT':([41,42,69,70,94,95,98,99,115,125,135,140,142,146,147,151,152,153,158,159,161,163,164,166,167,169,170,171,],[-72,-15,105,-26,-24,-25,-34,-35,-33,-32,105,105,-36,-72,-42,105,-40,-44,-39,105,-37,105,-41,-72,-38,105,105,-43,]),'ELSE':([42,94,98,99,115,125,142,146,147,152,153,158,161,164,167,171,],[-15,-24,-34,-35,-33,-32,-36,-72,-42,159,-44,-39,-37,-41,-38,-43,]),'ELSEIF':([42,94,98,99,115,125,142,146,147,152,153,158,161,164,167,171,],[-15,-24,-34,-35,-33,-32,-36,-72,-42,160,-44,-39,-37,-41,-38,-43,]),'WHERE':([42,70,94,95,98,99,115,125,142,143,146,147,148,149,152,153,155,158,161,164,166,167,169,171,],[-15,-26,-24,-25,-34,-35,-33,-32,-36,-72,-72,-42,156,-31,-40,-44,-30,-39,-37,-41,-72,-38,-29,-43,]),'IN':([129,],[138,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declist':([0,],[2,]),'dec':([0,2,],[4,12,]),'vardec':([0,2,69,135,140,151,159,163,169,170,],[5,5,99,99,99,99,99,99,99,99,]),'funcdec':([0,2,],[6,6,]),'idlist':([0,2,69,135,140,151,159,163,169,170,],[7,7,7,7,7,7,7,7,7,7,]),'iddec':([0,2,15,69,135,140,151,159,163,169,170,],[10,10,25,10,10,10,10,10,10,10,10,]),'type':([14,71,108,122,],[21,106,123,133,]),'exp':([17,18,30,32,33,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,69,96,112,116,117,118,119,120,135,137,140,150,151,159,163,165,169,170,],[28,38,65,66,67,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,97,114,124,126,127,128,130,131,97,144,97,157,97,97,97,168,97,97,]),'lvalue':([17,18,30,32,33,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,69,96,112,116,117,118,119,120,135,137,140,150,151,159,163,165,169,170,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'const':([17,18,30,32,33,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,69,96,112,116,117,118,119,120,135,137,140,150,151,156,159,163,165,169,170,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,162,31,31,31,31,31,]),'block':([20,39,69,73,123,135,140,151,159,163,169,170,],[40,68,98,109,134,98,98,98,98,98,98,98,]),'paramdecs':([26,],[44,]),'paramdecslist':([26,],[45,]),'empty':([26,41,143,146,166,],[46,70,149,153,70,]),'paramdec':([26,74,],[47,110,]),'stmtlist':([41,166,],[69,169,]),'explist':([48,],[75,]),'stmt':([69,135,140,151,159,163,169,170,],[95,142,146,158,164,167,95,171,]),'cases':([143,],[148,]),'elseiflist':([146,],[152,]),'case':([148,],[155,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declist MAIN LRB RRB block','program',5,'p_program','parser.py',66),
  ('program -> MAIN LRB RRB block','program',4,'p_program','parser.py',67),
  ('declist -> dec','declist',1,'p_declist','parser.py',71),
  ('declist -> declist dec','declist',2,'p_declist','parser.py',72),
  ('dec -> vardec','dec',1,'p_dec','parser.py',76),
  ('dec -> funcdec','dec',1,'p_dec','parser.py',77),
  ('type -> INTEGER','type',1,'p_type','parser.py',82),
  ('type -> FLOAT','type',1,'p_type','parser.py',83),
  ('type -> BOOLEAN','type',1,'p_type','parser.py',84),
  ('iddec -> ID','iddec',1,'p_iddec','parser.py',88),
  ('iddec -> ID LSB exp RSB','iddec',4,'p_iddec','parser.py',89),
  ('iddec -> ID ASSIGN exp','iddec',3,'p_iddec','parser.py',90),
  ('idlist -> iddec','idlist',1,'p_idlist','parser.py',94),
  ('idlist -> idlist COMMA iddec','idlist',3,'p_idlist','parser.py',95),
  ('vardec -> idlist COLON type SEMICOLON','vardec',4,'p_vardec','parser.py',99),
  ('funcdec -> FUNCTION ID LRB paramdecs RRB COLON type block','funcdec',8,'p_funcdec','parser.py',103),
  ('funcdec -> FUNCTION ID LRB paramdecs RRB block','funcdec',6,'p_funcdec','parser.py',104),
  ('paramdecs -> paramdecslist','paramdecs',1,'p_paramdecs','parser.py',108),
  ('paramdecs -> empty','paramdecs',1,'p_paramdecs','parser.py',109),
  ('paramdecslist -> paramdec','paramdecslist',1,'p_paramdecslist','parser.py',113),
  ('paramdecslist -> paramdecslist COMMA paramdec','paramdecslist',3,'p_paramdecslist','parser.py',114),
  ('paramdec -> ID COLON type','paramdec',3,'p_paramdec','parser.py',118),
  ('paramdec -> ID LSB RSB COLON type','paramdec',5,'p_paramdec','parser.py',119),
  ('block -> LCB stmtlist RCB','block',3,'p_block','parser.py',123),
  ('stmtlist -> stmtlist stmt','stmtlist',2,'p_stmtlist','parser.py',127),
  ('stmtlist -> empty','stmtlist',1,'p_stmtlist','parser.py',128),
  ('lvalue -> ID','lvalue',1,'p_lvalue','parser.py',132),
  ('lvalue -> ID LSB exp RSB','lvalue',4,'p_lvalue','parser.py',133),
  ('case -> WHERE const COLON stmtlist','case',4,'p_case','parser.py',137),
  ('cases -> cases case','cases',2,'p_cases','parser.py',141),
  ('cases -> empty','cases',1,'p_cases','parser.py',142),
  ('stmt -> RETURN exp SEMICOLON','stmt',3,'p_stmt','parser.py',146),
  ('stmt -> exp SEMICOLON','stmt',2,'p_stmt','parser.py',147),
  ('stmt -> block','stmt',1,'p_stmt','parser.py',148),
  ('stmt -> vardec','stmt',1,'p_stmt','parser.py',149),
  ('stmt -> WHILE LRB exp RRB stmt','stmt',5,'p_stmt','parser.py',150),
  ('stmt -> ON LRB exp RRB LCB cases RCB SEMICOLON','stmt',8,'p_stmt','parser.py',151),
  ('stmt -> FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt','stmt',9,'p_stmt','parser.py',152),
  ('stmt -> FOR LRB ID IN ID RRB stmt','stmt',7,'p_stmt','parser.py',153),
  ('stmt -> IF LRB exp RRB stmt elseiflist','stmt',6,'p_stmt','parser.py',154),
  ('stmt -> IF LRB exp RRB stmt elseiflist ELSE stmt','stmt',8,'p_stmt','parser.py',155),
  ('stmt -> PRINT LRB ID RRB SEMICOLON','stmt',5,'p_stmt','parser.py',156),
  ('elseiflist -> elseiflist ELSEIF LRB exp RRB stmt','elseiflist',6,'p_elseiflist','parser.py',161),
  ('elseiflist -> empty','elseiflist',1,'p_elseiflist','parser.py',162),
  ('exp -> lvalue ASSIGN exp','exp',3,'p_exp','parser.py',166),
  ('exp -> exp GT exp','exp',3,'p_exp','parser.py',167),
  ('exp -> exp LT exp','exp',3,'p_exp','parser.py',168),
  ('exp -> exp NE exp','exp',3,'p_exp','parser.py',169),
  ('exp -> exp EQ exp','exp',3,'p_exp','parser.py',170),
  ('exp -> exp LE exp','exp',3,'p_exp','parser.py',171),
  ('exp -> exp GE exp','exp',3,'p_exp','parser.py',172),
  ('exp -> exp AND exp','exp',3,'p_exp','parser.py',173),
  ('exp -> exp OR exp','exp',3,'p_exp','parser.py',174),
  ('exp -> exp SUM exp','exp',3,'p_exp','parser.py',175),
  ('exp -> exp SUB exp','exp',3,'p_exp','parser.py',176),
  ('exp -> exp MUL exp','exp',3,'p_exp','parser.py',177),
  ('exp -> exp DIV exp','exp',3,'p_exp','parser.py',178),
  ('exp -> exp MOD exp','exp',3,'p_exp','parser.py',179),
  ('exp -> const','exp',1,'p_exp','parser.py',180),
  ('exp -> lvalue','exp',1,'p_exp','parser.py',181),
  ('exp -> ID LRB explist RRB','exp',4,'p_exp','parser.py',182),
  ('exp -> LRB exp RRB','exp',3,'p_exp','parser.py',183),
  ('exp -> ID LRB RRB','exp',3,'p_exp','parser.py',184),
  ('exp -> SUB exp','exp',2,'p_exp','parser.py',185),
  ('exp -> NOT exp','exp',2,'p_exp','parser.py',186),
  ('const -> INTEGERNUMBER','const',1,'p_const','parser.py',191),
  ('const -> FLOATNUMBER','const',1,'p_const','parser.py',192),
  ('const -> TRUE','const',1,'p_const','parser.py',193),
  ('const -> FALSE','const',1,'p_const','parser.py',194),
  ('explist -> exp','explist',1,'p_explist','parser.py',198),
  ('explist -> explist COMMA exp','explist',3,'p_explist','parser.py',199),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',203),
]
