
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftWHILEFORONleftINleftIFleftELSEleftELSEIFleftWHEREleftPRINTleftRETURNrightASSIGNleftORleftANDleftGTLTNEEQLEGEleftMODleftSUMSUBleftMULDIVleftLCBRCBleftLSBRSBleftLRBRRBleftINTEGERNUMBERleftFLOATNUMBERleftTRUEFALSEleftINTEGERleftFLOATleftBOOLEANleftIDleftFUNCTIONleftMAINleftSEMICOLONCOLONleftERRORAND ASSIGN BOOLEAN COLON COMMA DIV ELSE ELSEIF EQ ERROR FALSE FLOAT FLOATNUMBER FOR FUNCTION GE GT ID IF IN INTEGER INTEGERNUMBER LCB LE LRB LSB LT MAIN MOD MUL NE NOT ON OR PRINT RCB RETURN RRB RSB SEMICOLON SUB SUM TRUE WHERE WHILEprogram : declist MAIN LRB RRB block\n                    | MAIN LRB RRB blockdeclist : dec\n                   | declist decdec : vardec\n               | funcdectype : INTEGER\n                | FLOAT\n                | BOOLEANiddec : ID\n                 | ID LSB exp RSB\n                 | ID ASSIGN expidlist : iddec\n                  | idlist COMMA iddecvardec : idlist COLON type SEMICOLONfuncdec : FUNCTION ID LRB paramdecs RRB COLON type block\n                   | FUNCTION ID LRB paramdecs RRB blockparamdecs : paramdecslist\n                     | emptyparamdecslist : paramdec\n                         | paramdecslist COMMA paramdec paramdec : ID COLON type\n                     | ID LSB RSB COLON typeblock : LCB stmtlist RCBstmtlist : stmtlist stmt\n                    | emptylvalue : ID\n                  | ID LSB exp RSBcase : WHERE const COLON stmtlistcases : cases case\n                | emptystmt : RETURN exp SEMICOLON\n                | exp SEMICOLON\n                | block\n                | vardec\n                | WHILE LRB exp RRB stmt\n                | ON LRB exp RRB LCB cases RCB SEMICOLON\n                | FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt\n                | FOR LRB ID IN ID RRB stmt\n                | IF LRB exp RRB stmt elseiflist\n                | IF LRB exp RRB stmt elseiflist ELSE stmt\n                | PRINT LRB ID RRBelseiflist : elseiflist ELSEIF LRB exp RRB stmt\n                      | emptyrelopexp : exp relop exp\n                    | relopexp relop expexp : lvalue ASSIGN exp\n               | exp operator exp\n               | relopexp\n               | const\n               | lvalue\n               | ID LRB explist RRB\n               | LRB exp RRB\n               | ID LRB RRB\n               | SUB exp\n               | NOT expoperator : AND\n                    | OR\n                    | SUM\n                    | SUB\n                    | MUL\n                    | DIV\n                    | MODconst : INTEGERNUMBER\n                 | FLOATNUMBER\n                 | TRUE\n                 | FALSErelop : GT\n                 | LT\n                 | NE\n                 | EQ\n                 | LE\n                 | GEexplist : exp\n                   | explist COMMA expempty :'
    
_lr_action_items = {'MAIN':([0,2,4,5,6,12,43,88,103,128,],[3,11,-3,-5,-6,-4,-15,-24,-17,-16,]),'FUNCTION':([0,2,4,5,6,12,43,88,103,128,],[8,8,-3,-5,-6,-4,-15,-24,-17,-16,]),'ID':([0,2,4,5,6,8,12,15,17,18,26,32,33,34,42,43,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,73,74,78,88,89,90,92,93,103,106,109,110,111,112,113,114,115,119,128,129,131,132,134,135,136,140,143,144,145,146,151,152,154,156,157,158,159,160,162,163,164,],[9,9,-3,-5,-6,16,-4,9,27,27,44,27,27,27,-76,-15,27,27,27,27,-57,-58,-59,-60,-61,-62,-63,-68,-69,-70,-71,-72,-73,27,27,97,-26,44,-24,-25,27,-34,-35,-17,27,-33,27,27,123,27,27,126,-32,-16,97,27,139,97,-42,-36,-76,27,97,-40,-44,-39,97,-37,97,-41,27,-76,-38,97,97,-43,]),'$end':([1,41,72,88,],[0,-2,-1,-24,]),'LRB':([3,11,16,17,18,27,32,33,34,42,43,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,73,74,88,89,90,92,93,94,95,96,97,98,99,106,109,110,111,112,113,114,119,123,129,131,134,135,136,140,143,144,145,146,151,152,153,154,156,157,158,159,160,162,163,164,],[13,19,26,32,32,49,32,32,32,-76,-15,32,32,32,32,-57,-58,-59,-60,-61,-62,-63,-68,-69,-70,-71,-72,-73,32,32,32,-26,-24,-25,32,-34,-35,110,111,112,49,114,115,32,-33,32,32,32,32,32,-32,49,32,32,32,-42,-36,-76,32,32,-40,-44,-39,32,158,-37,32,-41,32,-76,-38,32,32,-43,]),'COLON':([7,9,10,25,27,29,30,31,35,36,37,38,39,44,51,70,71,77,80,83,84,85,86,87,97,101,105,107,133,155,],[14,-10,-13,-14,-27,-51,-49,-50,-64,-65,-66,-67,-12,75,-11,-55,-56,102,-54,-48,-45,-47,-46,-53,-10,116,-52,-28,-11,159,]),'COMMA':([7,9,10,22,23,24,25,27,29,30,31,35,36,37,38,39,46,48,51,70,71,79,80,81,83,84,85,86,87,97,100,104,105,107,118,127,133,],[15,-10,-13,-7,-8,-9,-14,-27,-51,-49,-50,-64,-65,-66,-67,-12,78,-20,-11,-55,-56,106,-54,-74,-48,-45,-47,-46,-53,-10,-22,-21,-52,-28,-75,-23,-11,]),'LSB':([9,27,44,97,123,],[17,50,76,113,50,]),'ASSIGN':([9,27,29,97,107,123,133,],[18,-27,67,-27,-28,-27,-28,]),'RRB':([13,19,22,23,24,26,27,29,30,31,35,36,37,38,45,46,47,48,49,69,70,71,79,80,81,83,84,85,86,87,100,104,105,107,118,120,121,125,126,127,139,150,161,],[20,40,-7,-8,-9,-76,-27,-51,-49,-50,-64,-65,-66,-67,77,-18,-19,-20,80,87,-55,-56,105,-54,-74,-48,-45,-47,-46,-53,-22,-21,-52,-28,-75,129,130,134,135,-23,144,156,163,]),'INTEGER':([14,75,102,116,],[22,22,22,22,]),'FLOAT':([14,75,102,116,],[23,23,23,23,]),'BOOLEAN':([14,75,102,116,],[24,24,24,24,]),'SUB':([17,18,27,28,29,30,31,32,33,34,35,36,37,38,39,42,43,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,73,74,80,81,82,83,84,85,86,87,88,89,90,91,92,93,97,105,106,107,108,109,110,111,112,113,114,118,119,120,121,122,123,124,125,129,131,133,134,135,136,138,140,143,144,145,146,150,151,152,154,156,157,158,159,160,161,162,163,164,],[33,33,-27,57,-51,-49,-50,33,33,33,-64,-65,-66,-67,57,-76,-15,33,33,33,33,-57,-58,-59,-60,-61,-62,-63,-68,-69,-70,-71,-72,-73,33,33,57,-55,57,33,-26,-54,57,57,57,57,57,57,-53,-24,-25,33,57,-34,-35,-27,-52,33,-28,57,-33,33,33,33,33,33,57,-32,57,57,57,-27,57,57,33,33,-28,33,-42,-36,57,-76,33,33,-40,-44,57,-39,33,-37,33,-41,33,-76,-38,57,33,33,-43,]),'NOT':([17,18,32,33,34,42,43,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,73,74,88,89,90,92,93,106,109,110,111,112,113,114,119,129,131,134,135,136,140,143,144,145,146,151,152,154,156,157,158,159,160,162,163,164,],[34,34,34,34,34,-76,-15,34,34,34,34,-57,-58,-59,-60,-61,-62,-63,-68,-69,-70,-71,-72,-73,34,34,34,-26,-24,-25,34,-34,-35,34,-33,34,34,34,34,34,-32,34,34,34,-42,-36,-76,34,34,-40,-44,-39,34,-37,34,-41,34,-76,-38,34,34,-43,]),'INTEGERNUMBER':([17,18,32,33,34,42,43,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,73,74,88,89,90,92,93,106,109,110,111,112,113,114,119,129,131,134,135,136,140,143,144,145,146,149,151,152,154,156,157,158,159,160,162,163,164,],[35,35,35,35,35,-76,-15,35,35,35,35,-57,-58,-59,-60,-61,-62,-63,-68,-69,-70,-71,-72,-73,35,35,35,-26,-24,-25,35,-34,-35,35,-33,35,35,35,35,35,-32,35,35,35,-42,-36,-76,35,35,-40,-44,35,-39,35,-37,35,-41,35,-76,-38,35,35,-43,]),'FLOATNUMBER':([17,18,32,33,34,42,43,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,73,74,88,89,90,92,93,106,109,110,111,112,113,114,119,129,131,134,135,136,140,143,144,145,146,149,151,152,154,156,157,158,159,160,162,163,164,],[36,36,36,36,36,-76,-15,36,36,36,36,-57,-58,-59,-60,-61,-62,-63,-68,-69,-70,-71,-72,-73,36,36,36,-26,-24,-25,36,-34,-35,36,-33,36,36,36,36,36,-32,36,36,36,-42,-36,-76,36,36,-40,-44,36,-39,36,-37,36,-41,36,-76,-38,36,36,-43,]),'TRUE':([17,18,32,33,34,42,43,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,73,74,88,89,90,92,93,106,109,110,111,112,113,114,119,129,131,134,135,136,140,143,144,145,146,149,151,152,154,156,157,158,159,160,162,163,164,],[37,37,37,37,37,-76,-15,37,37,37,37,-57,-58,-59,-60,-61,-62,-63,-68,-69,-70,-71,-72,-73,37,37,37,-26,-24,-25,37,-34,-35,37,-33,37,37,37,37,37,-32,37,37,37,-42,-36,-76,37,37,-40,-44,37,-39,37,-37,37,-41,37,-76,-38,37,37,-43,]),'FALSE':([17,18,32,33,34,42,43,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,73,74,88,89,90,92,93,106,109,110,111,112,113,114,119,129,131,134,135,136,140,143,144,145,146,149,151,152,154,156,157,158,159,160,162,163,164,],[38,38,38,38,38,-76,-15,38,38,38,38,-57,-58,-59,-60,-61,-62,-63,-68,-69,-70,-71,-72,-73,38,38,38,-26,-24,-25,38,-34,-35,38,-33,38,38,38,38,38,-32,38,38,38,-42,-36,-76,38,38,-40,-44,38,-39,38,-37,38,-41,38,-76,-38,38,38,-43,]),'LCB':([20,22,23,24,40,42,43,73,74,77,88,89,92,93,109,117,119,129,130,134,135,136,140,144,145,146,151,152,154,156,157,159,160,162,163,164,],[42,-7,-8,-9,42,-76,-15,42,-26,42,-24,-25,-34,-35,-33,42,-32,42,137,42,-42,-36,-76,42,-40,-44,-39,42,-37,42,-41,-76,-38,42,42,-43,]),'SEMICOLON':([21,22,23,24,27,29,30,31,35,36,37,38,70,71,80,83,84,85,86,87,91,97,105,107,108,122,123,133,138,147,],[43,-7,-8,-9,-27,-51,-49,-50,-64,-65,-66,-67,-55,-56,-54,-48,-45,-47,-46,-53,109,-27,-52,-28,119,131,-27,-28,143,154,]),'RSB':([27,28,29,30,31,35,36,37,38,70,71,76,80,82,83,84,85,86,87,105,107,124,],[-27,51,-51,-49,-50,-64,-65,-66,-67,-55,-56,101,-54,107,-48,-45,-47,-46,-53,-52,-28,133,]),'AND':([27,28,29,30,31,35,36,37,38,39,69,70,71,80,81,82,83,84,85,86,87,91,97,105,107,108,118,120,121,122,123,124,125,133,138,150,161,],[-27,54,-51,-49,-50,-64,-65,-66,-67,54,54,-55,54,-54,54,54,54,54,54,54,-53,54,-27,-52,-28,54,54,54,54,54,-27,54,54,-28,54,54,54,]),'OR':([27,28,29,30,31,35,36,37,38,39,69,70,71,80,81,82,83,84,85,86,87,91,97,105,107,108,118,120,121,122,123,124,125,133,138,150,161,],[-27,55,-51,-49,-50,-64,-65,-66,-67,55,55,-55,55,-54,55,55,55,55,55,55,-53,55,-27,-52,-28,55,55,55,55,55,-27,55,55,-28,55,55,55,]),'SUM':([27,28,29,30,31,35,36,37,38,39,69,70,71,80,81,82,83,84,85,86,87,91,97,105,107,108,118,120,121,122,123,124,125,133,138,150,161,],[-27,56,-51,-49,-50,-64,-65,-66,-67,56,56,-55,56,-54,56,56,56,56,56,56,-53,56,-27,-52,-28,56,56,56,56,56,-27,56,56,-28,56,56,56,]),'MUL':([27,28,29,30,31,35,36,37,38,39,69,70,71,80,81,82,83,84,85,86,87,91,97,105,107,108,118,120,121,122,123,124,125,133,138,150,161,],[-27,58,-51,-49,-50,-64,-65,-66,-67,58,58,58,58,-54,58,58,58,58,58,58,-53,58,-27,-52,-28,58,58,58,58,58,-27,58,58,-28,58,58,58,]),'DIV':([27,28,29,30,31,35,36,37,38,39,69,70,71,80,81,82,83,84,85,86,87,91,97,105,107,108,118,120,121,122,123,124,125,133,138,150,161,],[-27,59,-51,-49,-50,-64,-65,-66,-67,59,59,59,59,-54,59,59,59,59,59,59,-53,59,-27,-52,-28,59,59,59,59,59,-27,59,59,-28,59,59,59,]),'MOD':([27,28,29,30,31,35,36,37,38,39,69,70,71,80,81,82,83,84,85,86,87,91,97,105,107,108,118,120,121,122,123,124,125,133,138,150,161,],[-27,60,-51,-49,-50,-64,-65,-66,-67,60,60,-55,60,-54,60,60,60,60,60,60,-53,60,-27,-52,-28,60,60,60,60,60,-27,60,60,-28,60,60,60,]),'GT':([27,28,29,30,31,35,36,37,38,39,69,70,71,80,81,82,83,84,85,86,87,91,97,105,107,108,118,120,121,122,123,124,125,133,138,150,161,],[-27,61,-51,61,-50,-64,-65,-66,-67,61,61,-55,61,-54,61,61,61,61,61,61,-53,61,-27,-52,-28,61,61,61,61,61,-27,61,61,-28,61,61,61,]),'LT':([27,28,29,30,31,35,36,37,38,39,69,70,71,80,81,82,83,84,85,86,87,91,97,105,107,108,118,120,121,122,123,124,125,133,138,150,161,],[-27,62,-51,62,-50,-64,-65,-66,-67,62,62,-55,62,-54,62,62,62,62,62,62,-53,62,-27,-52,-28,62,62,62,62,62,-27,62,62,-28,62,62,62,]),'NE':([27,28,29,30,31,35,36,37,38,39,69,70,71,80,81,82,83,84,85,86,87,91,97,105,107,108,118,120,121,122,123,124,125,133,138,150,161,],[-27,63,-51,63,-50,-64,-65,-66,-67,63,63,-55,63,-54,63,63,63,63,63,63,-53,63,-27,-52,-28,63,63,63,63,63,-27,63,63,-28,63,63,63,]),'EQ':([27,28,29,30,31,35,36,37,38,39,69,70,71,80,81,82,83,84,85,86,87,91,97,105,107,108,118,120,121,122,123,124,125,133,138,150,161,],[-27,64,-51,64,-50,-64,-65,-66,-67,64,64,-55,64,-54,64,64,64,64,64,64,-53,64,-27,-52,-28,64,64,64,64,64,-27,64,64,-28,64,64,64,]),'LE':([27,28,29,30,31,35,36,37,38,39,69,70,71,80,81,82,83,84,85,86,87,91,97,105,107,108,118,120,121,122,123,124,125,133,138,150,161,],[-27,65,-51,65,-50,-64,-65,-66,-67,65,65,-55,65,-54,65,65,65,65,65,65,-53,65,-27,-52,-28,65,65,65,65,65,-27,65,65,-28,65,65,65,]),'GE':([27,28,29,30,31,35,36,37,38,39,69,70,71,80,81,82,83,84,85,86,87,91,97,105,107,108,118,120,121,122,123,124,125,133,138,150,161,],[-27,66,-51,66,-50,-64,-65,-66,-67,66,66,-55,66,-54,66,66,66,66,66,66,-53,66,-27,-52,-28,66,66,66,66,66,-27,66,66,-28,66,66,66,]),'RCB':([42,43,73,74,88,89,92,93,109,119,135,136,137,140,141,142,145,146,148,151,154,157,159,160,162,164,],[-76,-15,88,-26,-24,-25,-34,-35,-33,-32,-42,-36,-76,-76,147,-31,-40,-44,-30,-39,-37,-41,-76,-38,-29,-43,]),'RETURN':([42,43,73,74,88,89,92,93,109,119,129,134,135,136,140,144,145,146,151,152,154,156,157,159,160,162,163,164,],[-76,-15,90,-26,-24,-25,-34,-35,-33,-32,90,90,-42,-36,-76,90,-40,-44,-39,90,-37,90,-41,-76,-38,90,90,-43,]),'WHILE':([42,43,73,74,88,89,92,93,109,119,129,134,135,136,140,144,145,146,151,152,154,156,157,159,160,162,163,164,],[-76,-15,94,-26,-24,-25,-34,-35,-33,-32,94,94,-42,-36,-76,94,-40,-44,-39,94,-37,94,-41,-76,-38,94,94,-43,]),'ON':([42,43,73,74,88,89,92,93,109,119,129,134,135,136,140,144,145,146,151,152,154,156,157,159,160,162,163,164,],[-76,-15,95,-26,-24,-25,-34,-35,-33,-32,95,95,-42,-36,-76,95,-40,-44,-39,95,-37,95,-41,-76,-38,95,95,-43,]),'FOR':([42,43,73,74,88,89,92,93,109,119,129,134,135,136,140,144,145,146,151,152,154,156,157,159,160,162,163,164,],[-76,-15,96,-26,-24,-25,-34,-35,-33,-32,96,96,-42,-36,-76,96,-40,-44,-39,96,-37,96,-41,-76,-38,96,96,-43,]),'IF':([42,43,73,74,88,89,92,93,109,119,129,134,135,136,140,144,145,146,151,152,154,156,157,159,160,162,163,164,],[-76,-15,98,-26,-24,-25,-34,-35,-33,-32,98,98,-42,-36,-76,98,-40,-44,-39,98,-37,98,-41,-76,-38,98,98,-43,]),'PRINT':([42,43,73,74,88,89,92,93,109,119,129,134,135,136,140,144,145,146,151,152,154,156,157,159,160,162,163,164,],[-76,-15,99,-26,-24,-25,-34,-35,-33,-32,99,99,-42,-36,-76,99,-40,-44,-39,99,-37,99,-41,-76,-38,99,99,-43,]),'ELSE':([43,88,92,93,109,119,135,136,140,145,146,151,154,157,160,164,],[-15,-24,-34,-35,-33,-32,-42,-36,-76,-40,-44,-39,-37,-41,-38,-43,]),'ELSEIF':([43,88,92,93,109,119,135,136,140,145,146,151,154,157,160,164,],[-15,-24,-34,-35,-33,-32,-42,-36,-76,-40,-44,-39,-37,-41,-38,-43,]),'WHERE':([43,74,88,89,92,93,109,119,135,136,137,140,141,142,145,146,148,151,154,157,159,160,162,164,],[-15,-26,-24,-25,-34,-35,-33,-32,-42,-36,-76,-76,149,-31,-40,-44,-30,-39,-37,-41,-76,-38,-29,-43,]),'IN':([123,],[132,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declist':([0,],[2,]),'dec':([0,2,],[4,12,]),'vardec':([0,2,73,129,134,144,152,156,162,163,],[5,5,93,93,93,93,93,93,93,93,]),'funcdec':([0,2,],[6,6,]),'idlist':([0,2,73,129,134,144,152,156,162,163,],[7,7,7,7,7,7,7,7,7,7,]),'iddec':([0,2,15,73,129,134,144,152,156,162,163,],[10,10,25,10,10,10,10,10,10,10,10,]),'type':([14,75,102,116,],[21,100,117,127,]),'exp':([17,18,32,33,34,49,50,52,53,67,68,73,90,106,110,111,112,113,114,129,131,134,143,144,152,156,158,162,163,],[28,39,69,70,71,81,82,83,84,85,86,91,108,118,120,121,122,124,125,91,138,91,150,91,91,91,161,91,91,]),'lvalue':([17,18,32,33,34,49,50,52,53,67,68,73,90,106,110,111,112,113,114,129,131,134,143,144,152,156,158,162,163,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'relopexp':([17,18,32,33,34,49,50,52,53,67,68,73,90,106,110,111,112,113,114,129,131,134,143,144,152,156,158,162,163,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'const':([17,18,32,33,34,49,50,52,53,67,68,73,90,106,110,111,112,113,114,129,131,134,143,144,149,152,156,158,162,163,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,155,31,31,31,31,31,]),'block':([20,40,73,77,117,129,134,144,152,156,162,163,],[41,72,92,103,128,92,92,92,92,92,92,92,]),'paramdecs':([26,],[45,]),'paramdecslist':([26,],[46,]),'empty':([26,42,137,140,159,],[47,74,142,146,74,]),'paramdec':([26,78,],[48,104,]),'operator':([28,39,69,70,71,81,82,83,84,85,86,91,108,118,120,121,122,124,125,138,150,161,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'relop':([28,30,39,69,70,71,81,82,83,84,85,86,91,108,118,120,121,122,124,125,138,150,161,],[53,68,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'stmtlist':([42,159,],[73,162,]),'explist':([49,],[79,]),'stmt':([73,129,134,144,152,156,162,163,],[89,136,140,151,157,160,89,164,]),'cases':([137,],[141,]),'elseiflist':([140,],[145,]),'case':([141,],[148,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declist MAIN LRB RRB block','program',5,'p_program','parser.py',64),
  ('program -> MAIN LRB RRB block','program',4,'p_program','parser.py',65),
  ('declist -> dec','declist',1,'p_declist','parser.py',69),
  ('declist -> declist dec','declist',2,'p_declist','parser.py',70),
  ('dec -> vardec','dec',1,'p_dec','parser.py',74),
  ('dec -> funcdec','dec',1,'p_dec','parser.py',75),
  ('type -> INTEGER','type',1,'p_type','parser.py',80),
  ('type -> FLOAT','type',1,'p_type','parser.py',81),
  ('type -> BOOLEAN','type',1,'p_type','parser.py',82),
  ('iddec -> ID','iddec',1,'p_iddec','parser.py',86),
  ('iddec -> ID LSB exp RSB','iddec',4,'p_iddec','parser.py',87),
  ('iddec -> ID ASSIGN exp','iddec',3,'p_iddec','parser.py',88),
  ('idlist -> iddec','idlist',1,'p_idlist','parser.py',92),
  ('idlist -> idlist COMMA iddec','idlist',3,'p_idlist','parser.py',93),
  ('vardec -> idlist COLON type SEMICOLON','vardec',4,'p_vardec','parser.py',97),
  ('funcdec -> FUNCTION ID LRB paramdecs RRB COLON type block','funcdec',8,'p_funcdec','parser.py',101),
  ('funcdec -> FUNCTION ID LRB paramdecs RRB block','funcdec',6,'p_funcdec','parser.py',102),
  ('paramdecs -> paramdecslist','paramdecs',1,'p_paramdecs','parser.py',106),
  ('paramdecs -> empty','paramdecs',1,'p_paramdecs','parser.py',107),
  ('paramdecslist -> paramdec','paramdecslist',1,'p_paramdecslist','parser.py',111),
  ('paramdecslist -> paramdecslist COMMA paramdec','paramdecslist',3,'p_paramdecslist','parser.py',112),
  ('paramdec -> ID COLON type','paramdec',3,'p_paramdec','parser.py',116),
  ('paramdec -> ID LSB RSB COLON type','paramdec',5,'p_paramdec','parser.py',117),
  ('block -> LCB stmtlist RCB','block',3,'p_block','parser.py',121),
  ('stmtlist -> stmtlist stmt','stmtlist',2,'p_stmtlist','parser.py',125),
  ('stmtlist -> empty','stmtlist',1,'p_stmtlist','parser.py',126),
  ('lvalue -> ID','lvalue',1,'p_lvalue','parser.py',130),
  ('lvalue -> ID LSB exp RSB','lvalue',4,'p_lvalue','parser.py',131),
  ('case -> WHERE const COLON stmtlist','case',4,'p_case','parser.py',135),
  ('cases -> cases case','cases',2,'p_cases','parser.py',139),
  ('cases -> empty','cases',1,'p_cases','parser.py',140),
  ('stmt -> RETURN exp SEMICOLON','stmt',3,'p_stmt','parser.py',145),
  ('stmt -> exp SEMICOLON','stmt',2,'p_stmt','parser.py',146),
  ('stmt -> block','stmt',1,'p_stmt','parser.py',147),
  ('stmt -> vardec','stmt',1,'p_stmt','parser.py',148),
  ('stmt -> WHILE LRB exp RRB stmt','stmt',5,'p_stmt','parser.py',149),
  ('stmt -> ON LRB exp RRB LCB cases RCB SEMICOLON','stmt',8,'p_stmt','parser.py',150),
  ('stmt -> FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt','stmt',9,'p_stmt','parser.py',151),
  ('stmt -> FOR LRB ID IN ID RRB stmt','stmt',7,'p_stmt','parser.py',152),
  ('stmt -> IF LRB exp RRB stmt elseiflist','stmt',6,'p_stmt','parser.py',153),
  ('stmt -> IF LRB exp RRB stmt elseiflist ELSE stmt','stmt',8,'p_stmt','parser.py',154),
  ('stmt -> PRINT LRB ID RRB','stmt',4,'p_stmt','parser.py',155),
  ('elseiflist -> elseiflist ELSEIF LRB exp RRB stmt','elseiflist',6,'p_elseiflist','parser.py',160),
  ('elseiflist -> empty','elseiflist',1,'p_elseiflist','parser.py',161),
  ('relopexp -> exp relop exp','relopexp',3,'p_relopexp','parser.py',166),
  ('relopexp -> relopexp relop exp','relopexp',3,'p_relopexp','parser.py',167),
  ('exp -> lvalue ASSIGN exp','exp',3,'p_exp','parser.py',172),
  ('exp -> exp operator exp','exp',3,'p_exp','parser.py',173),
  ('exp -> relopexp','exp',1,'p_exp','parser.py',174),
  ('exp -> const','exp',1,'p_exp','parser.py',175),
  ('exp -> lvalue','exp',1,'p_exp','parser.py',176),
  ('exp -> ID LRB explist RRB','exp',4,'p_exp','parser.py',177),
  ('exp -> LRB exp RRB','exp',3,'p_exp','parser.py',178),
  ('exp -> ID LRB RRB','exp',3,'p_exp','parser.py',179),
  ('exp -> SUB exp','exp',2,'p_exp','parser.py',180),
  ('exp -> NOT exp','exp',2,'p_exp','parser.py',181),
  ('operator -> AND','operator',1,'p_operator','parser.py',185),
  ('operator -> OR','operator',1,'p_operator','parser.py',186),
  ('operator -> SUM','operator',1,'p_operator','parser.py',187),
  ('operator -> SUB','operator',1,'p_operator','parser.py',188),
  ('operator -> MUL','operator',1,'p_operator','parser.py',189),
  ('operator -> DIV','operator',1,'p_operator','parser.py',190),
  ('operator -> MOD','operator',1,'p_operator','parser.py',191),
  ('const -> INTEGERNUMBER','const',1,'p_const','parser.py',195),
  ('const -> FLOATNUMBER','const',1,'p_const','parser.py',196),
  ('const -> TRUE','const',1,'p_const','parser.py',197),
  ('const -> FALSE','const',1,'p_const','parser.py',198),
  ('relop -> GT','relop',1,'p_relop','parser.py',202),
  ('relop -> LT','relop',1,'p_relop','parser.py',203),
  ('relop -> NE','relop',1,'p_relop','parser.py',204),
  ('relop -> EQ','relop',1,'p_relop','parser.py',205),
  ('relop -> LE','relop',1,'p_relop','parser.py',206),
  ('relop -> GE','relop',1,'p_relop','parser.py',207),
  ('explist -> exp','explist',1,'p_explist','parser.py',211),
  ('explist -> explist COMMA exp','explist',3,'p_explist','parser.py',212),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',216),
]