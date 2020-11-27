
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftLCBRCBleftLSBRSBleftLRBRRBleftELSEIFELSEleftIFleftORleftANDleftNOTleftGTLTNEEQLEGEleftMODleftSUMSUBleftMULDIVleftINTEGERNUMBERleftFLOATNUMBERleftTRUEFALSEleftIDrightASSIGNleftERRORAND ASSIGN BOOLEAN COLON COMMA DIV ELSE ELSEIF EQ ERROR FALSE FLOAT FLOATNUMBER FOR FUNCTION GE GT ID IF IN INTEGER INTEGERNUMBER LCB LE LRB LSB LT MAIN MOD MUL NE NOT ON OR PRINT RCB RETURN RRB RSB SEMICOLON SUB SUM TRUE WHERE WHILEprogram : declist MAIN LRB RRB block\n                    | MAIN LRB RRB blockdeclist : dec\n                   | declist decdec : vardec\n               | funcdectype : INTEGER\n                | FLOAT\n                | BOOLEANiddec : lvalue\n                 | lvalue ASSIGN expidlist : iddec\n                  | idlist COMMA iddecvardec : idlist COLON type SEMICOLONfuncdec : FUNCTION ID LRB paramdecs RRB COLON type block\n                   | FUNCTION ID LRB paramdecs RRB blockparamdecs : paramdecslist\n                     | emptyparamdecslist : paramdec\n                         | paramdecslist COMMA paramdec paramdec : ID COLON type\n                     | ID LSB RSB COLON typeblock : LCB stmtlist RCBstmtlist : stmtlist stmt\n                    | emptylvalue : ID\n                  | ID LSB exp RSBcase : WHERE const COLON stmtlistcases : cases case\n                | emptystmt : RETURN exp SEMICOLON\n                | exp SEMICOLON\n                | block\n                | vardec\n                | WHILE LRB exp RRB stmt\n                | ON LRB exp RRB LCB cases RCB SEMICOLON\n                | FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt\n                | FOR LRB ID IN ID RRB stmt\n                | IF LRB exp RRB stmt elseiflist\n                | IF LRB exp RRB stmt elseiflist ELSE stmt\n                | PRINT LRB ID RRB SEMICOLONelseiflist : elseiflist ELSEIF LRB exp RRB stmt\n                      | emptyexp : lvalue ASSIGN exp\n               | exp GT exp\n               | exp LT exp\n               | exp NE exp\n               | exp EQ exp\n               | exp LE exp\n               | exp GE exp\n               | exp AND exp\n               | exp OR exp\n               | exp SUM exp\n               | exp SUB exp\n               | exp MUL exp\n               | exp DIV exp\n               | exp MOD exp\n               | const\n               | lvalue\n               | lvalue LRB explist RRB\n               | LRB exp RRB\n               | lvalue LRB RRB\n               | SUB exp\n               | NOT expconst : INTEGERNUMBER\n                 | FLOATNUMBER\n                 | TRUE\n                 | FALSEexplist : exp\n                   | explist COMMA expempty :'
    
_lr_action_items = {'MAIN':([0,2,4,5,6,13,42,92,107,131,],[3,12,-3,-5,-6,-4,-14,-23,-16,-15,]),'FUNCTION':([0,2,4,5,6,13,42,92,107,131,],[8,8,-3,-5,-6,-4,-14,-23,-16,-15,]),'ID':([0,2,4,5,6,8,13,16,18,19,27,30,32,33,41,42,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,68,69,73,92,93,94,96,97,107,110,112,113,114,115,116,117,118,122,131,132,134,135,136,138,142,143,146,147,148,149,154,155,157,159,160,161,162,163,165,166,167,],[9,9,-3,-5,-6,17,-4,9,9,9,43,9,9,9,-71,-14,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,-25,43,-23,-24,9,-33,-34,-16,9,-32,9,9,126,9,128,9,-31,-15,9,9,141,9,-35,-71,-41,9,9,-39,-43,-38,9,-36,9,-40,9,-71,-37,9,9,-42,]),'$end':([1,40,67,92,],[0,-2,-1,-23,]),'LRB':([3,9,12,17,18,19,29,30,32,33,41,42,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,68,69,92,93,94,96,97,98,99,100,101,102,103,110,112,113,114,115,116,118,122,126,132,134,136,138,142,143,146,147,148,149,154,155,156,157,159,160,161,162,163,165,166,167,],[14,-26,20,27,32,32,63,32,32,32,-71,-14,-27,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-25,-23,-24,32,-33,-34,113,114,115,116,117,63,32,-32,32,32,32,32,32,-31,-26,32,32,32,-35,-71,-41,32,32,-39,-43,-38,32,161,-36,32,-40,32,-71,-37,32,32,-42,]),'COLON':([7,9,10,11,26,29,31,34,35,36,37,38,43,48,64,66,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,91,103,105,109,129,158,],[15,-26,-12,-10,-13,-59,-58,-65,-66,-67,-68,-11,70,-27,-63,-64,106,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-44,-62,-61,-10,119,-60,-11,162,]),'COMMA':([7,9,10,11,23,24,25,26,29,31,34,35,36,37,38,45,47,48,64,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,103,104,108,109,121,129,130,],[16,-26,-12,-10,-7,-8,-9,-13,-59,-58,-65,-66,-67,-68,-11,73,-19,-27,-63,-64,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-44,110,-62,-69,-61,-10,-21,-20,-60,-70,-11,-22,]),'ASSIGN':([9,11,29,48,103,126,],[-26,19,62,-27,118,-26,]),'RSB':([9,28,29,31,34,35,36,37,48,64,66,71,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,91,109,],[-26,48,-59,-58,-65,-66,-67,-68,-27,-63,-64,105,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-44,-62,-61,-60,]),'GT':([9,28,29,31,34,35,36,37,38,48,64,65,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,90,91,95,103,109,111,121,123,124,125,126,127,129,140,153,164,],[-26,49,-59,-58,-65,-66,-67,-68,49,-27,-63,49,49,-45,-46,-47,-48,-49,-50,49,49,-53,-54,-55,-56,-57,-44,-62,49,-61,49,-59,-60,49,49,49,49,49,-26,49,-44,49,49,49,]),'LT':([9,28,29,31,34,35,36,37,38,48,64,65,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,90,91,95,103,109,111,121,123,124,125,126,127,129,140,153,164,],[-26,50,-59,-58,-65,-66,-67,-68,50,-27,-63,50,50,-45,-46,-47,-48,-49,-50,50,50,-53,-54,-55,-56,-57,-44,-62,50,-61,50,-59,-60,50,50,50,50,50,-26,50,-44,50,50,50,]),'NE':([9,28,29,31,34,35,36,37,38,48,64,65,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,90,91,95,103,109,111,121,123,124,125,126,127,129,140,153,164,],[-26,51,-59,-58,-65,-66,-67,-68,51,-27,-63,51,51,-45,-46,-47,-48,-49,-50,51,51,-53,-54,-55,-56,-57,-44,-62,51,-61,51,-59,-60,51,51,51,51,51,-26,51,-44,51,51,51,]),'EQ':([9,28,29,31,34,35,36,37,38,48,64,65,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,90,91,95,103,109,111,121,123,124,125,126,127,129,140,153,164,],[-26,52,-59,-58,-65,-66,-67,-68,52,-27,-63,52,52,-45,-46,-47,-48,-49,-50,52,52,-53,-54,-55,-56,-57,-44,-62,52,-61,52,-59,-60,52,52,52,52,52,-26,52,-44,52,52,52,]),'LE':([9,28,29,31,34,35,36,37,38,48,64,65,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,90,91,95,103,109,111,121,123,124,125,126,127,129,140,153,164,],[-26,53,-59,-58,-65,-66,-67,-68,53,-27,-63,53,53,-45,-46,-47,-48,-49,-50,53,53,-53,-54,-55,-56,-57,-44,-62,53,-61,53,-59,-60,53,53,53,53,53,-26,53,-44,53,53,53,]),'GE':([9,28,29,31,34,35,36,37,38,48,64,65,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,90,91,95,103,109,111,121,123,124,125,126,127,129,140,153,164,],[-26,54,-59,-58,-65,-66,-67,-68,54,-27,-63,54,54,-45,-46,-47,-48,-49,-50,54,54,-53,-54,-55,-56,-57,-44,-62,54,-61,54,-59,-60,54,54,54,54,54,-26,54,-44,54,54,54,]),'AND':([9,28,29,31,34,35,36,37,38,48,64,65,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,90,91,95,103,109,111,121,123,124,125,126,127,129,140,153,164,],[-26,55,-59,-58,-65,-66,-67,-68,55,-27,-63,55,-64,-45,-46,-47,-48,-49,-50,-51,55,-53,-54,-55,-56,-57,-44,-62,55,-61,55,-59,-60,55,55,55,55,55,-26,55,-44,55,55,55,]),'OR':([9,28,29,31,34,35,36,37,38,48,64,65,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,90,91,95,103,109,111,121,123,124,125,126,127,129,140,153,164,],[-26,56,-59,-58,-65,-66,-67,-68,56,-27,-63,56,-64,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-44,-62,56,-61,56,-59,-60,56,56,56,56,56,-26,56,-44,56,56,56,]),'SUM':([9,28,29,31,34,35,36,37,38,48,64,65,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,90,91,95,103,109,111,121,123,124,125,126,127,129,140,153,164,],[-26,57,-59,-58,-65,-66,-67,-68,57,-27,-63,57,57,57,57,57,57,57,57,57,57,-53,-54,-55,-56,57,-44,-62,57,-61,57,-59,-60,57,57,57,57,57,-26,57,-44,57,57,57,]),'SUB':([9,18,19,28,29,30,31,32,33,34,35,36,37,38,41,42,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,90,91,92,93,94,95,96,97,103,109,110,111,112,113,114,115,116,118,121,122,123,124,125,126,127,129,132,134,136,138,140,142,143,146,147,148,149,153,154,155,157,159,160,161,162,163,164,165,166,167,],[-26,30,30,58,-59,30,-58,30,30,-65,-66,-67,-68,58,-71,-14,-27,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,-63,58,58,30,-25,58,58,58,58,58,58,58,58,-53,-54,-55,-56,58,-44,-62,58,-61,-23,-24,30,58,-33,-34,-59,-60,30,58,-32,30,30,30,30,30,58,-31,58,58,58,-26,58,-44,30,30,30,-35,58,-71,-41,30,30,-39,-43,58,-38,30,-36,30,-40,30,-71,-37,58,30,30,-42,]),'MUL':([9,28,29,31,34,35,36,37,38,48,64,65,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,90,91,95,103,109,111,121,123,124,125,126,127,129,140,153,164,],[-26,59,-59,-58,-65,-66,-67,-68,59,-27,59,59,59,59,59,59,59,59,59,59,59,59,59,-55,-56,59,-44,-62,59,-61,59,-59,-60,59,59,59,59,59,-26,59,-44,59,59,59,]),'DIV':([9,28,29,31,34,35,36,37,38,48,64,65,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,90,91,95,103,109,111,121,123,124,125,126,127,129,140,153,164,],[-26,60,-59,-58,-65,-66,-67,-68,60,-27,60,60,60,60,60,60,60,60,60,60,60,60,60,-55,-56,60,-44,-62,60,-61,60,-59,-60,60,60,60,60,60,-26,60,-44,60,60,60,]),'MOD':([9,28,29,31,34,35,36,37,38,48,64,65,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,90,91,95,103,109,111,121,123,124,125,126,127,129,140,153,164,],[-26,61,-59,-58,-65,-66,-67,-68,61,-27,-63,61,61,61,61,61,61,61,61,61,61,-53,-54,-55,-56,-57,-44,-62,61,-61,61,-59,-60,61,61,61,61,61,-26,61,-44,61,61,61,]),'RRB':([9,14,20,23,24,25,27,29,31,34,35,36,37,44,45,46,47,48,63,64,65,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,104,108,109,121,123,124,127,128,130,141,153,164,],[-26,21,39,-7,-8,-9,-71,-59,-58,-65,-66,-67,-68,72,-17,-18,-19,-27,89,-63,91,-64,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-44,109,-62,-69,-61,-21,-20,-60,-70,132,133,136,137,-22,147,159,166,]),'SEMICOLON':([9,22,23,24,25,29,31,34,35,36,37,48,64,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,91,95,103,109,111,125,126,129,137,140,150,],[-26,42,-7,-8,-9,-59,-58,-65,-66,-67,-68,-27,-63,-64,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-44,-62,-61,112,-59,-60,122,134,-26,-44,143,146,157,]),'LSB':([9,43,126,],[18,71,18,]),'INTEGER':([15,70,106,119,],[23,23,23,23,]),'FLOAT':([15,70,106,119,],[24,24,24,24,]),'BOOLEAN':([15,70,106,119,],[25,25,25,25,]),'NOT':([18,19,30,32,33,41,42,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,68,69,92,93,94,96,97,110,112,113,114,115,116,118,122,132,134,136,138,142,143,146,147,148,149,154,155,157,159,160,161,162,163,165,166,167,],[33,33,33,33,33,-71,-14,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,-25,-23,-24,33,-33,-34,33,-32,33,33,33,33,33,-31,33,33,33,-35,-71,-41,33,33,-39,-43,-38,33,-36,33,-40,33,-71,-37,33,33,-42,]),'INTEGERNUMBER':([18,19,30,32,33,41,42,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,68,69,92,93,94,96,97,110,112,113,114,115,116,118,122,132,134,136,138,142,143,146,147,148,149,152,154,155,157,159,160,161,162,163,165,166,167,],[34,34,34,34,34,-71,-14,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,-25,-23,-24,34,-33,-34,34,-32,34,34,34,34,34,-31,34,34,34,-35,-71,-41,34,34,-39,-43,34,-38,34,-36,34,-40,34,-71,-37,34,34,-42,]),'FLOATNUMBER':([18,19,30,32,33,41,42,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,68,69,92,93,94,96,97,110,112,113,114,115,116,118,122,132,134,136,138,142,143,146,147,148,149,152,154,155,157,159,160,161,162,163,165,166,167,],[35,35,35,35,35,-71,-14,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,-25,-23,-24,35,-33,-34,35,-32,35,35,35,35,35,-31,35,35,35,-35,-71,-41,35,35,-39,-43,35,-38,35,-36,35,-40,35,-71,-37,35,35,-42,]),'TRUE':([18,19,30,32,33,41,42,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,68,69,92,93,94,96,97,110,112,113,114,115,116,118,122,132,134,136,138,142,143,146,147,148,149,152,154,155,157,159,160,161,162,163,165,166,167,],[36,36,36,36,36,-71,-14,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-25,-23,-24,36,-33,-34,36,-32,36,36,36,36,36,-31,36,36,36,-35,-71,-41,36,36,-39,-43,36,-38,36,-36,36,-40,36,-71,-37,36,36,-42,]),'FALSE':([18,19,30,32,33,41,42,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,68,69,92,93,94,96,97,110,112,113,114,115,116,118,122,132,134,136,138,142,143,146,147,148,149,152,154,155,157,159,160,161,162,163,165,166,167,],[37,37,37,37,37,-71,-14,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,-25,-23,-24,37,-33,-34,37,-32,37,37,37,37,37,-31,37,37,37,-35,-71,-41,37,37,-39,-43,37,-38,37,-36,37,-40,37,-71,-37,37,37,-42,]),'LCB':([21,23,24,25,39,41,42,68,69,72,92,93,96,97,112,120,122,132,133,136,138,142,143,147,148,149,154,155,157,159,160,162,163,165,166,167,],[41,-7,-8,-9,41,-71,-14,41,-25,41,-23,-24,-33,-34,-32,41,-31,41,139,41,-35,-71,-41,41,-39,-43,-38,41,-36,41,-40,-71,-37,41,41,-42,]),'RCB':([41,42,68,69,92,93,96,97,112,122,138,139,142,143,144,145,148,149,151,154,157,160,162,163,165,167,],[-71,-14,92,-25,-23,-24,-33,-34,-32,-31,-35,-71,-71,-41,150,-30,-39,-43,-29,-38,-36,-40,-71,-37,-28,-42,]),'RETURN':([41,42,68,69,92,93,96,97,112,122,132,136,138,142,143,147,148,149,154,155,157,159,160,162,163,165,166,167,],[-71,-14,94,-25,-23,-24,-33,-34,-32,-31,94,94,-35,-71,-41,94,-39,-43,-38,94,-36,94,-40,-71,-37,94,94,-42,]),'WHILE':([41,42,68,69,92,93,96,97,112,122,132,136,138,142,143,147,148,149,154,155,157,159,160,162,163,165,166,167,],[-71,-14,98,-25,-23,-24,-33,-34,-32,-31,98,98,-35,-71,-41,98,-39,-43,-38,98,-36,98,-40,-71,-37,98,98,-42,]),'ON':([41,42,68,69,92,93,96,97,112,122,132,136,138,142,143,147,148,149,154,155,157,159,160,162,163,165,166,167,],[-71,-14,99,-25,-23,-24,-33,-34,-32,-31,99,99,-35,-71,-41,99,-39,-43,-38,99,-36,99,-40,-71,-37,99,99,-42,]),'FOR':([41,42,68,69,92,93,96,97,112,122,132,136,138,142,143,147,148,149,154,155,157,159,160,162,163,165,166,167,],[-71,-14,100,-25,-23,-24,-33,-34,-32,-31,100,100,-35,-71,-41,100,-39,-43,-38,100,-36,100,-40,-71,-37,100,100,-42,]),'IF':([41,42,68,69,92,93,96,97,112,122,132,136,138,142,143,147,148,149,154,155,157,159,160,162,163,165,166,167,],[-71,-14,101,-25,-23,-24,-33,-34,-32,-31,101,101,-35,-71,-41,101,-39,-43,-38,101,-36,101,-40,-71,-37,101,101,-42,]),'PRINT':([41,42,68,69,92,93,96,97,112,122,132,136,138,142,143,147,148,149,154,155,157,159,160,162,163,165,166,167,],[-71,-14,102,-25,-23,-24,-33,-34,-32,-31,102,102,-35,-71,-41,102,-39,-43,-38,102,-36,102,-40,-71,-37,102,102,-42,]),'ELSE':([42,92,96,97,112,122,138,142,143,148,149,154,157,160,163,167,],[-14,-23,-33,-34,-32,-31,-35,-71,-41,155,-43,-38,-36,-40,-37,-42,]),'ELSEIF':([42,92,96,97,112,122,138,142,143,148,149,154,157,160,163,167,],[-14,-23,-33,-34,-32,-31,-35,-71,-41,156,-43,-38,-36,-40,-37,-42,]),'WHERE':([42,69,92,93,96,97,112,122,138,139,142,143,144,145,148,149,151,154,157,160,162,163,165,167,],[-14,-25,-23,-24,-33,-34,-32,-31,-35,-71,-71,-41,152,-30,-39,-43,-29,-38,-36,-40,-71,-37,-28,-42,]),'IN':([126,],[135,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declist':([0,],[2,]),'dec':([0,2,],[4,13,]),'vardec':([0,2,68,132,136,147,155,159,165,166,],[5,5,97,97,97,97,97,97,97,97,]),'funcdec':([0,2,],[6,6,]),'idlist':([0,2,68,132,136,147,155,159,165,166,],[7,7,7,7,7,7,7,7,7,7,]),'iddec':([0,2,16,68,132,136,147,155,159,165,166,],[10,10,26,10,10,10,10,10,10,10,10,]),'lvalue':([0,2,16,18,19,30,32,33,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,68,94,110,113,114,115,116,118,132,134,136,146,147,155,159,161,165,166,],[11,11,11,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,103,29,29,29,29,29,29,29,103,29,103,29,103,103,103,29,103,103,]),'type':([15,70,106,119,],[22,104,120,130,]),'exp':([18,19,30,32,33,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,68,94,110,113,114,115,116,118,132,134,136,146,147,155,159,161,165,166,],[28,38,64,65,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,90,95,111,121,123,124,125,127,129,95,140,95,153,95,95,95,164,95,95,]),'const':([18,19,30,32,33,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,68,94,110,113,114,115,116,118,132,134,136,146,147,152,155,159,161,165,166,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,158,31,31,31,31,31,]),'block':([21,39,68,72,120,132,136,147,155,159,165,166,],[40,67,96,107,131,96,96,96,96,96,96,96,]),'paramdecs':([27,],[44,]),'paramdecslist':([27,],[45,]),'empty':([27,41,139,142,162,],[46,69,145,149,69,]),'paramdec':([27,73,],[47,108,]),'stmtlist':([41,162,],[68,165,]),'explist':([63,],[88,]),'stmt':([68,132,136,147,155,159,165,166,],[93,138,142,154,160,163,93,167,]),'cases':([139,],[144,]),'elseiflist':([142,],[148,]),'case':([144,],[151,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declist MAIN LRB RRB block','program',5,'p_program','parser.py',65),
  ('program -> MAIN LRB RRB block','program',4,'p_program','parser.py',66),
  ('declist -> dec','declist',1,'p_declist','parser.py',70),
  ('declist -> declist dec','declist',2,'p_declist','parser.py',71),
  ('dec -> vardec','dec',1,'p_dec','parser.py',75),
  ('dec -> funcdec','dec',1,'p_dec','parser.py',76),
  ('type -> INTEGER','type',1,'p_type','parser.py',81),
  ('type -> FLOAT','type',1,'p_type','parser.py',82),
  ('type -> BOOLEAN','type',1,'p_type','parser.py',83),
  ('iddec -> lvalue','iddec',1,'p_iddec','parser.py',87),
  ('iddec -> lvalue ASSIGN exp','iddec',3,'p_iddec','parser.py',88),
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
  ('stmt -> RETURN exp SEMICOLON','stmt',3,'p_stmt','parser.py',144),
  ('stmt -> exp SEMICOLON','stmt',2,'p_stmt','parser.py',145),
  ('stmt -> block','stmt',1,'p_stmt','parser.py',146),
  ('stmt -> vardec','stmt',1,'p_stmt','parser.py',147),
  ('stmt -> WHILE LRB exp RRB stmt','stmt',5,'p_stmt','parser.py',148),
  ('stmt -> ON LRB exp RRB LCB cases RCB SEMICOLON','stmt',8,'p_stmt','parser.py',149),
  ('stmt -> FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt','stmt',9,'p_stmt','parser.py',150),
  ('stmt -> FOR LRB ID IN ID RRB stmt','stmt',7,'p_stmt','parser.py',151),
  ('stmt -> IF LRB exp RRB stmt elseiflist','stmt',6,'p_stmt','parser.py',152),
  ('stmt -> IF LRB exp RRB stmt elseiflist ELSE stmt','stmt',8,'p_stmt','parser.py',153),
  ('stmt -> PRINT LRB ID RRB SEMICOLON','stmt',5,'p_stmt','parser.py',154),
  ('elseiflist -> elseiflist ELSEIF LRB exp RRB stmt','elseiflist',6,'p_elseiflist','parser.py',159),
  ('elseiflist -> empty','elseiflist',1,'p_elseiflist','parser.py',160),
  ('exp -> lvalue ASSIGN exp','exp',3,'p_exp','parser.py',164),
  ('exp -> exp GT exp','exp',3,'p_exp','parser.py',165),
  ('exp -> exp LT exp','exp',3,'p_exp','parser.py',166),
  ('exp -> exp NE exp','exp',3,'p_exp','parser.py',167),
  ('exp -> exp EQ exp','exp',3,'p_exp','parser.py',168),
  ('exp -> exp LE exp','exp',3,'p_exp','parser.py',169),
  ('exp -> exp GE exp','exp',3,'p_exp','parser.py',170),
  ('exp -> exp AND exp','exp',3,'p_exp','parser.py',171),
  ('exp -> exp OR exp','exp',3,'p_exp','parser.py',172),
  ('exp -> exp SUM exp','exp',3,'p_exp','parser.py',173),
  ('exp -> exp SUB exp','exp',3,'p_exp','parser.py',174),
  ('exp -> exp MUL exp','exp',3,'p_exp','parser.py',175),
  ('exp -> exp DIV exp','exp',3,'p_exp','parser.py',176),
  ('exp -> exp MOD exp','exp',3,'p_exp','parser.py',177),
  ('exp -> const','exp',1,'p_exp','parser.py',178),
  ('exp -> lvalue','exp',1,'p_exp','parser.py',179),
  ('exp -> lvalue LRB explist RRB','exp',4,'p_exp','parser.py',180),
  ('exp -> LRB exp RRB','exp',3,'p_exp','parser.py',181),
  ('exp -> lvalue LRB RRB','exp',3,'p_exp','parser.py',182),
  ('exp -> SUB exp','exp',2,'p_exp','parser.py',183),
  ('exp -> NOT exp','exp',2,'p_exp','parser.py',184),
  ('const -> INTEGERNUMBER','const',1,'p_const','parser.py',189),
  ('const -> FLOATNUMBER','const',1,'p_const','parser.py',190),
  ('const -> TRUE','const',1,'p_const','parser.py',191),
  ('const -> FALSE','const',1,'p_const','parser.py',192),
  ('explist -> exp','explist',1,'p_explist','parser.py',196),
  ('explist -> explist COMMA exp','explist',3,'p_explist','parser.py',197),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',201),
]
