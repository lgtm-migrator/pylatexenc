# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
# 
# Copyright (c) 2015 Philippe Faist
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#


from __future__ import print_function, absolute_import
import unicodedata;
import logging
import sys
if sys.version_info.major > 2:
    def unicode(string): return string
    basestring = str

log = logging.getLogger(__name__)


#
# CHARACTER MAP TAKEN FROM latexcodec 0.2, by Peter Troeger
#    https://pypi.python.org/pypi/latexcodec
#
#
# latexcodec is a lexer and codec to work with LaTeX code in Python
# Copyright (c) 2011-2014 by Matthias C. M. Troffaes
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# 
#

# generated by genmapping.py
utf82latex={
34:"''", 	# character "
35:'\\#', 	# character #
36:'\\$', 	# character $
37:'\\%', 	# character %
38:'\\&', 	# character &
95:'\\_', 	# character _
123:'\\{', 	# character {
125:'\\}', 	# character }
160:'~', 	# character  
161:'\\textexclamdown', 	# character ¡
162:'\\textcent', 	# character ¢
163:'\\textsterling', 	# character £
164:'\\textcurrency', 	# character €
165:'\\textyen', 	# character ¥
166:'\\textbrokenbar', 	# character Š
167:'\\textsection', 	# character §
168:'\\textasciidieresis', 	# character š
169:'\\textcopyright', 	# character ©
170:'\\textordfeminine', 	# character ª
171:'\\guillemotleft', 	# character «
172:'\\textlnot', 	# character ¬
174:'\\textregistered', 	# character ®
175:'\\textasciimacron', 	# character ¯
176:'\\textdegree', 	# character °
177:'\\ensuremath{\\pm}', 	# character ±
178:'\\texttwosuperior', 	# character ²
179:'\\textthreesuperior', 	# character ³
180:'\\textasciiacute', 	# character Ž
181:'\\textmu', 	# character µ
182:'\\textparagraph', 	# character ¶
183:'\\textperiodcentered', 	# character ·
185:'\\textonesuperior', 	# character ¹
186:'\\textordmasculine', 	# character º
187:'\\guillemotright', 	# character »
188:'\\textonequarter', 	# character Œ
189:'\\textonehalf', 	# character œ
190:'\\textthreequarters', 	# character Ÿ
191:'\\textquestiondown', 	# character ¿
192:'\\`A', 	# character À
193:"\\'A", 	# character Á
194:'\\^A', 	# character Â
195:'\\~A', 	# character Ã
196:'\\"A', 	# character Ä
197:'\\r{A}', 	# character Å
198:'\\AE', 	# character Æ
199:'\\c{C}', 	# character Ç
200:'\\`E', 	# character È
201:"\\'E", 	# character É
202:'\\^E', 	# character Ê
203:'\\"E', 	# character Ë
204:'\\`I', 	# character Ì
205:"\\'I", 	# character Í
206:'\\^I', 	# character Î
207:'\\"I', 	# character Ï
208:'\\DH', 	# character Ð
209:'\\~N', 	# character Ñ
210:'\\`O', 	# character Ò
211:"\\'O", 	# character Ó
212:'\\^O', 	# character Ô
213:'\\~O', 	# character Õ
214:'\\"O', 	# character Ö
215:'\\texttimes', 	# character ×
216:'\\O', 	# character Ø
217:'\\`U', 	# character Ù
218:"\\'U", 	# character Ú
219:'\\^U', 	# character Û
220:'\\"U', 	# character Ü
221:"\\'Y", 	# character Ý
222:'\\TH', 	# character Þ
223:'\\ss', 	# character ß
224:'\\`a', 	# character à
225:"\\'a", 	# character á
226:'\\^a', 	# character â
227:'\\~a', 	# character ã
228:'\\"a', 	# character ä
229:'\\r{a}', 	# character å
230:'\\ae', 	# character æ
231:'\\c{c}', 	# character ç
232:'\\`e', 	# character è
233:"\\'e", 	# character é
234:'\\^e', 	# character ê
235:'\\"e', 	# character ë
236:'\\`\\i', 	# character ì
237:"\\'\\i", 	# character í
238:'\\^\\i', 	# character î
239:'\\"\\i', 	# character ï
240:'\\dh', 	# character ð
241:'\\~n', 	# character ñ
242:'\\`o', 	# character ò
243:"\\'o", 	# character ó
244:'\\^o', 	# character ô
245:'\\~o', 	# character õ
246:'\\"o', 	# character ö
247:'\\textdiv', 	# character ÷
248:'\\o', 	# character ø
249:'\\`u', 	# character ù
250:"\\'u", 	# character ú
251:'\\^u', 	# character û
252:'\\"u', 	# character ü
253:"\\'y", 	# character ý
254:'\\th', 	# character þ
255:'\\"y', 	# character ÿ
256:'\\={A}',
257:'\\={a}',
258:'\\u{A}',
259:'\\u{a}',
260:'\\k{A}',
261:'\\k{a}',
262:"\\'C",
263:"\\'c",
264:'\\^{C}',
265:'\\^{c}',
266:'\\.{C}',
267:'\\.{c}',
268:'\\v{C}',
269:'\\v{c}',
270:'\\v{D}',
271:'\\v{d}',
272:'\\DJ',
273:'\\dj',
274:'\\={E}',
275:'\\={e}',
276:'\\u{E}',
277:'\\u{e}',
278:'\\.{E}',
279:'\\.{e}',
280:'\\k{E}',
281:'\\k{e}',
282:'\\v{E}',
283:'\\v{e}',
284:'\\^{G}',
285:'\\^{g}',
286:'\\u{G}',
287:'\\u{g}',
288:'\\.{G}',
289:'\\.{g}',
290:'\\c{G}',
291:'\\c{g}',
292:'\\^{H}',
293:'\\^{h}',
294:'\\={H}',
295:'\\={h}',
296:'\\~{I}',
297:'\\~{i}',
298:'\\={I}',
299:'\\={i}',
300:'\\u{I}',
301:'\\u{i}',
302:'\\k{I}',
303:'\\k{i}',
304:'\\.I',
305:'\\i',
306:'\\IJ',
307:'\\ij',
308:'\\^{J}',
309:'\\^{j}',
310:'\\c{K}',
311:'\\c{k}',
312:'\\textsc\{k\}',
313:"\\'L",
314:"\\'l",
315:'\\c{L}',
316:'\\c{l}',
317:'\\v{L}',
318:'\\v{l}',
319:'\\.{L}',
320:'\\.{l}',
321:'\\L',
322:'\\l',
323:"\\'N",
324:"\\'n",
325:'\\c{N}',
326:'\\c{n}',
327:'\\v{N}',
328:'\\v{n}',
329:'\\nument{149}',
330:'\\NG',
331:'\\ng',
332:'\\={O}',
333:'\\={o}',
334:'\\u{O}',
335:'\\u{o}',
336:"\\'{O}",
337:"\\'{o}",
338:'\\OE',
339:'\\oe',
340:"\\'R",
341:"\\'r",
342:'\\c{R}',
343:'\\c{r}',
344:'\\v{R}',
345:'\\v{r}',
346:"\\'S",
347:"\\'s",
348:'\\^{S}',
349:'\\^{s}',
350:'\\c{S}',
351:'\\c{s}',
352:'\\v{S}',
353:'\\v{s}',
354:'\\c{T}',
355:'\\c{t}',
356:'\\v{T}',
357:'\\v{t}',
358:'\\={T}',
359:'\\={t}',
360:'\\~{U}',
361:'\\~{u}',
362:'\\={U}',
363:'\\={u}',
364:'\\u{U}',
365:'\\u{u}',
366:'\\r{U}',
367:'\\r{u}',
368:"\\'{U}",
369:"\\'{u}",
370:'\\k{U}',
371:'\\k{u}',
372:'\\^{W}',
373:'\\^{w}',
374:'\\^{Y}',
375:'\\^{y}',
376:'\\"Y',
377:"\\'Z",
378:"\\'z",
379:'\\.Z',
380:'\\.z',
381:'\\v{Z}',
382:'\\v{z}',
402:'\\textflorin',
710:'\\textasciicircum',
711:'\\textasciicaron',
728:'\\textasciibreve',
732:'\\textasciitilde',
733:'\\textacutedbl',
1024:'\\`\\CYRE',
1025:'\\CYRYO',
1026:'\\CYRDJE',
1027:'\\`\\CYRG',
1028:'\\CYRIE',
1029:'\\CYRDZE',
1030:'\\CYRII',
1031:'\\CYRYI',
1032:'\\CYRJE',
1033:'\\CYRLJE',
1034:'\\CYRNJE',
1035:'\\CYRTSHE',
1036:'\\`\\CYRK',
1037:'\\`\\CYRI',
1038:'\\CYRUSHRT',
1039:'\\CYRDZHE',
1040:'\\CYRA',
1041:'\\CYRB',
1042:'\\CYRV',
1043:'\\CYRG',
1044:'\\CYRD',
1045:'\\CYRE',
1046:'\\CYRZH',
1047:'\\CYRZ',
1048:'\\CYRI',
1049:'\\CYRISHRT',
1050:'\\CYRK',
1051:'\\CYRL',
1052:'\\CYRM',
1053:'\\CYRN',
1054:'\\CYRO',
1055:'\\CYRP',
1056:'\\CYRR',
1057:'\\CYRS',
1058:'\\CYRT',
1059:'\\CYRU',
1060:'\\CYRF',
1061:'\\CYRH',
1062:'\\CYRC',
1063:'\\CYRCH',
1064:'\\CYRSH',
1065:'\\CYRSHCH',
1066:'\\CYRHRDSN',
1067:'\\CYRERY',
1068:'\\CYRSFTSN',
1069:'\\CYREREV',
1070:'\\CYRYU',
1071:'\\CYRYA',
1072:'\\cyra',
1073:'\\cyrb',
1074:'\\cyrv',
1075:'\\cyrg',
1076:'\\cyrd',
1077:'\\cyre',
1078:'\\cyrzh',
1079:'\\cyrz',
1080:'\\cyri',
1081:'\\cyrishrt',
1082:'\\cyrk',
1083:'\\cyrl',
1084:'\\cyrm',
1085:'\\cyrn',
1086:'\\cyro',
1087:'\\cyrp',
1088:'\\cyrr',
1089:'\\cyrs',
1090:'\\cyrt',
1091:'\\cyru',
1092:'\\cyrf',
1093:'\\cyrh',
1094:'\\cyrc',
1095:'\\cyrch',
1096:'\\cyrsh',
1097:'\\cyrshch',
1098:'\\cyrhrdsn',
1099:'\\cyrery',
1100:'\\cyrsftsn',
1101:'\\cyrerev',
1102:'\\cyryu',
1103:'\\cyrya',
1104:'\\`\\cyre',
1105:'\\cyryo',
1106:'\\cyrdje',
1107:'\\`\\cyrg',
1108:'\\cyrie',
1109:'\\cyrdze',
1110:'\\cyrii',
1111:'\\cyryi',
1112:'\\cyrje',
1113:'\\cyrlje',
1114:'\\cyrnje',
1115:'\\cyrtshe',
1116:'\\`\\cyrk',
1117:'\\`\\cyri',
1118:'\\cyrushrt',
1119:'\\cyrdzhe',
1122:'\\CYRYAT',
1123:'\\cyryat',
1130:'\\CYRBYUS',
1131:'\\cyrbyus',
1138:'\\CYRFITA',
1139:'\\cyrfita',
1140:'\\CYRIZH',
1141:'\\cyrizh',
1142:'\\C\\CYRIZH',
1143:'\\C\\cyrizh',
1164:'\\CYRSEMISFTSN',
1165:'\\cyrsemisftsn',
1166:'\\CYRRTICK',
1167:'\\cyrrtick',
1168:'\\CYRGUP',
1169:'\\cyrgup',
1170:'\\CYRGHCRS',
1171:'\\cyrghcrs',
1172:'\\CYRGHK',
1173:'\\cyrghk',
1174:'\\CYRZHDSC',
1175:'\\cyrzhdsc',
1176:'\\CYRZDSC',
1177:'\\cyrzdsc',
1178:'\\CYRKDSC',
1179:'\\cyrkdsc',
1180:'\\CYRKVCRS',
1181:'\\cyrkvcrs',
1182:'\\CYRKHCRS',
1183:'\\cyrkhcrs',
1184:'\\CYRKBEAK',
1185:'\\cyrkbeak',
1186:'\\CYRNDSC',
1187:'\\cyrndsc',
1188:'\\CYRNG',
1189:'\\cyrng',
1190:'\\CYRPHK',
1191:'\\cyrphk',
1192:'\\CYRABHHA',
1193:'\\cyrabhha',
1194:'\\CYRSDSC',
1195:'\\cyrsdsc',
1196:'\\CYRTDSC',
1197:'\\cyrtdsc',
1198:'\\CYRY',
1199:'\\cyry',
1200:'\\CYRYHCRS',
1201:'\\cyryhcrs',
1202:'\\CYRHDSC',
1203:'\\cyrhdsc',
1204:'\\CYRTETSE',
1205:'\\cyrtetse',
1206:'\\CYRCHRDSC',
1207:'\\cyrchrdsc',
1208:'\\CYRCHVCRS',
1209:'\\cyrchvcrs',
1210:'\\CYRSHHA',
1211:'\\cyrshha',
1212:'\\CYRABHCH',
1213:'\\cyrabhch',
1214:'\\CYRABHCHDSC',
1215:'\\cyrabhchdsc',
1216:'\\CYRpalochka',
1217:'\\U\\CYRZH',
1218:'\\U\\cyrzh',
1219:'\\CYRKHK',
1220:'\\cyrkhk',
1221:'\\CYRLDSC',
1222:'\\cyrldsc',
1223:'\\CYRNHK',
1224:'\\cyrnhk',
1227:'\\CYRCHLDSC',
1228:'\\cyrchldsc',
1229:'\\CYRMDSC',
1230:'\\cyrmdsc',
1232:'\\U\\CYRA',
1233:'\\U\\cyra',
1234:'\\"\\CYRA',
1235:'\\"\\cyra',
1236:'\\CYRAE',
1237:'\\cyrae',
1238:'\\U\\CYRE',
1239:'\\U\\cyre',
1240:'\\CYRSCHWA',
1241:'\\cyrschwa',
1242:'\\"\\CYRSCHWA',
1243:'\\"\\cyrschwa',
1244:'\\"\\CYRZH',
1245:'\\"\\cyrzh',
1246:'\\"\\CYRZ',
1247:'\\"\\cyrz',
1248:'\\CYRABHDZE',
1249:'\\cyrabhdze',
1250:'\\=\\CYRI',
1251:'\\=\\cyri',
1252:'\\"\\CYRI',
1253:'\\"\\cyri',
1254:'\\"\\CYRO',
1255:'\\"\\cyro',
1256:'\\CYROTLD',
1257:'\\cyrotld',
1260:'\\"\\CYREREV',
1261:'\\"\\cyrerev',
1262:'\\=\\CYRU',
1263:'\\=\\cyru',
1264:'\\"\\CYRU',
1265:'\\"\\cyru',
1266:'\\H\\CYRU',
1267:'\\H\\cyru',
1268:'\\"\\CYRCH',
1269:'\\"\\cyrch',
1270:'\\CYRGDSC',
1271:'\\cyrgdsc',
1272:'\\"\\CYRERY',
1273:'\\"\\cyrery',
1274:'\\CYRGDSCHCRS',
1275:'\\cyrgdschcrs',
1276:'\\CYRHHK',
1277:'\\cyrhhk',
1278:'\\CYRHHCRS',
1279:'\\cyrhhcrs',
3647:'\\textbaht',
8204:'\\textcompwordmark',
8211:'\\textendash',
8212:'\\textemdash',
8214:'\\textbardbl',
8216:'\\textquoteleft',
8217:'\\textquoteright',
8218:'\\quotesinglbase',
8220:'\\textquotedblleft',
8221:'\\textquotedblright',
8222:'\\quotedblbase',
8224:'\\textdagger',
8225:'\\textdaggerdbl',
8226:'\\textbullet',
8230:'\\textellipsis',
8240:'\\textperthousand',
8241:'\\textpertenthousand',
8249:'\\guilsinglleft',
8250:'\\guilsinglright',
8251:'\\textreferencemark',
8253:'\\textinterrobang',
8260:'\\textfractionsolidus',
8270:'\\textasteriskcentered',
8274:'\\textdiscount',
8353:'\\textcolonmonetary',
8356:'\\textlira',
8358:'\\textnaira',
8361:'\\textwon',
8363:'\\textdong',
8364:'\\texteuro',
8369:'\\textpeso',
8451:'\\textcelsius',
8470:'\\textnumero',
8471:'\\textcircledP',
8478:'\\textrecipe',
8480:'\\textservicemark',
8482:'\\texttrademark',
8486:'\\textohm',
8487:'\\textmho',
8494:'\\textestimated',
8592:'\\textleftarrow',
8593:'\\textuparrow',
8594:'\\textrightarrow',
8595:'\\textdownarrow',
9001:'\\textlangle',
9002:'\\textrangle',
9250:'\\textblank',
9251:'\\textvisiblespace',
9702:'\\textopenbullet',
9711:'\\textbigcircle',
9834:'\\textmusicalnote',


# ADDED MANUALLY (PhF):
# ---------------------

0x02BC: r"'", # MODIFIER LETTER APOSTROPHE

# Combining Diacritical Marks (!!TODO!! smarter)
0x0307: r'\ensuremath{\dot{}}',
0x0308: r'\ensuremath{\ddot{}}',

0x0391: r'A', # GREEK CAPITAL LETTER ALPHA
0x0392: r'B', # GREEK CAPITAL LETTER BETA
0x0393: r'\ensuremath{\Gamma}', # GREEK CAPITAL LETTER GAMMA
0x0394: r'\ensuremath{\Delta}', # ...
0x0395: r'E',
0x0396: r'Z',
0x0397: r'H',
0x0398: r'\ensuremath{\Theta}',
0x0399: r'I',
0x039A: r'K',
0x039B: r'\ensuremath{\Lambda}',
0x039C: r'M',
0x039D: r'N',
0x039E: r'\ensuremath{\Xi}',
0x039F: r'O',
0x03A0: r'\ensuremath{\Pi}',
0x03A1: r'P',
0x03A3: r'\ensuremath{\Sigma}',
0x03A4: r'T',
0x03A5: r'\ensuremath{\Upsilon}',
0x03A6: r'\ensuremath{\Phi}',
0x03A7: r'X',
0x03A8: r'\ensuremath{\Psi}',
0x03A9: r'\ensuremath{\Omega}',
# tonos letters [ ... ]
0x03B1: r'\ensuremath{\alpha}', # Greek Small Letter Alpha
0x03B2: r'\ensuremath{\beta}',
0x03B3: r'\ensuremath{\gamma}',
0x03B4: r'\ensuremath{\delta}',
0x03B5: r'\ensuremath{\varepsilon}',
0x03B6: r'\ensuremath{\zeta}',
0x03B7: r'\ensuremath{\eta}',
0x03B8: r'\ensuremath{\theta}',
0x03B9: r'\ensuremath{\i}',
0x03BA: r'\ensuremath{\kappa}',
0x03BB: r'\ensuremath{\lambda}',
0x03BC: r'\ensuremath{\mu}',
0x03BD: r'\ensuremath{\nu}',
0x03BE: r'\ensuremath{\xi}',
0x03BF: r'o',
0x03C0: r'\ensuremath{\pi}',
0x03C1: r'\ensuremath{\rho}',
0x03C2: r'\ensuremath{\varsigma}',
0x03C3: r'\ensuremath{\sigma}',
0x03C4: r'\ensuremath{\tau}',
0x03C5: r'\ensuremath{\upsilon}',
0x03C6: r'\ensuremath{\varphi}',
0x03C7: r'\ensuremath{\chi}',
0x03C8: r'\ensuremath{\psi}',
0x03C9: r'\ensuremath{\omega}',


0x03D1: r'\ensuremath{\vartheta}', # Greek Theta Symbol
0x03D5: r'\ensuremath{\phi}', # Greek Phi Symbol
0x03D6: r'\ensuremath{\varpi}', # Greek Pi Symbol
0x03F1: r'\ensuremath{\varrho}', # Greek rho symbol

# spaces
0x2000: r'\enskip', # EN QUAD (= EN SPACE U+2002)
0x2001: r'\quad', # EM QUAD (= EM SPACE U+2003)
0x2002: r'\enskip', # EN SPACE
0x2003: r'\quad', # EM SPACE
0x2004: r'\hspace{0.33em}', # THREE-PER-EM SPACE
0x2005: r'\hsapce{0.25em}', # FOUR-PER-EM SPACE
0x2006: r'\hspace{0.167em}', # SIX-PER-EM SPACE
0x2007: r'~', # FIGURE SPACE
0x2008: r'\;', # PUNCTUATION SPACE
0x2009: r'\,', # thin space
0x200A: r'\hspace{1pt}', # supposed to be thinnest typographical space available

0x2010: r'-', # HYPHEN
0x2061: r'', # FUNCTION APPLICATION

0x210F: r'\ensuremath{\hbar}', # h bar
0x2113: r'\ensuremath{\ell}', # SCRIPT SMALL L

# Math operators and symbols (U+22XX)
0x2200: r'\ensuremath{\forall}',
0x2201: r'\ensuremath{\complement}',
0x2202: r'\ensuremath{\partial}',
0x2203: r'\ensuremath{\exists}',
0x2204: r'\ensuremath{\nexists}',
0x2205: r'\ensuremath{\varnothing}',
0x2206: r'\ensuremath{\Delta}',
0x2207: r'\ensuremath{\nabla}',
0x2208: r'\ensuremath{\in}',
0x2209: r'\ensuremath{\notin}',
0x220A: r'\ensuremath{\in}', # alternative
0x220B: r'\ensuremath{\ni}',
0x220C: r'\ensuremath{\not\ni}',
0x220D: r'\ensuremath{\ni}', # alternative
0x220E: r'\ensuremath{\blacksquare}',
0x220F: r'\ensuremath{\prod}',
0x2210: r'\ensuremath{\coprod}',
0x2211: r'\ensuremath{\sum}',
0x2212: r'\ensuremath{-}',
0x2213: r'\ensuremath{\mp}',
#0x2214: DOT PLUS
0x2215: r'\ensuremath{/}',
0x2216: r'\ensuremath{\smallsetminus}',
0x2217: r'\ensuremath{*}',
0x2218: r'\ensuremath{\circ}',
0x2219: r'\ensuremath{\bullet}',
0x221A: r'\ensuremath{\sqrt{}}',
0x221B: r'\ensuremath{\sqrt[3]{}}',
0x221C: r'\ensuremath{\sqrt[4]{}}',
0x221D: r'\ensuremath{\propto}',
0x221E: r'\ensuremath{\infty}',
#0x221F: RIGHT ANGLE
#0x2220: ANGLE
#0x2221: MEASURED ANGLE
#0x2222: SPHERICAL ANGLE
0x2223: r'\ensuremath{\mid}',
0x2224: r'\ensuremath{\nmid}',
0x2225: r'\ensuremath{\parallel}',
0x2226: r'\ensuremath{\nparallel}',
0x2227: r'\ensuremath{\wedge}',
0x2228: r'\ensuremath{\vee}',
0x2229: r'\ensuremath{\cap}',
0x222A: r'\ensuremath{\cup}',
0x222B: r'\ensuremath{\int}',
0x222C: r'\ensuremath{\iint}',
0x222D: r'\ensuremath{\iiint}',
0x222E: r'\ensuremath{\oint}',
#0x222F: SURFACE INTEGRAL
#0x2230: VOLUME INTEGRAL
#0x2231: CLOCKWISE INTEGRAL
#0x2232: CLOCKWIZSE CONTOUR INTEGRAL
#0x2233: ANTICLOCKWISE CONTOUR INTEGRAL
0x2234: r'\ensuremath{\therefore}',
0x2235: r'\ensuremath{\because}',
0x2236: r'\ensuremath{:}',
0x2237: r'\ensuremath{::}',
#0x2238: DOT MINUS
#...
0x223C: r'\ensuremath{\sim}',
0x223D: r'\ensuremath{\backsim}',
#
0x2248: r'\ensuremath{\approx}',
#
0x2260: r'\ensuremath{\neq}',
0x2261: r'\ensuremath{\equiv}',
0x2262: r'\ensuremath{\not\equiv}',
#0x2263: STRICTLY EQUIVALENT TO
0x2264: r'\ensuremath{\leq}',
0x2265: r'\ensuremath{\geq}',
0x2266: r'\ensuremath{\leqq}',
0x2267: r'\ensuremath{\geqq}',
0x2268: r'\ensuremath{\lneqq}',
0x2269: r'\ensuremath{\gneqq}',
0x226A: r'\ensuremath{\ll}',
0x226B: r'\ensuremath{\gg}',
#0x226C: BETWEEN
#0x226D: NOT EQUIVLAENT TO
0x226E: r'\ensuremath{\nless}',
0x226F: r'\ensuremath{\ngtr}',
0x2270: r'\ensuremath{\nleq}',
0x2271: r'\ensuremath{\ngeq}',
0x2272: r'\ensuremath{\lesssim}',
0x2273: r'\ensuremath{\gtrsim}',
0x2274: r'\ensuremath{\not\lesssim}',
0x2275: r'\ensuremath{\not\gtrsim}',
0x2276: r'\ensuremath{\lessgtr}',
0x2277: r'\ensuremath{\gtrless}',
#0x2278: NEITHER LESS-THAN NOR GREATER-THAN
#0x2279: NEITHER GREATER-THAN NOR LESS-THAN
0x227A: r'\ensuremath{\prec}',
0x227B: r'\ensuremath{\succ}',
0x227C: r'\ensuremath{\preceq}',
0x227D: r'\ensuremath{\succeq}',
0x227E: r'\ensuremath{\precsim}',
0x227F: r'\ensuremath{\succsim}',
0x2280: r'\ensuremath{\nprec}',
0x2281: r'\ensuremath{\nsucc}',
0x2282: r'\ensuremath{\subset}',
0x2283: r'\ensuremath{\supset}',
0x2284: r'\ensuremath{\not\subset}',
0x2285: r'\ensuremath{\not\supset}',
0x2286: r'\ensuremath{\subseteq}',
0x2287: r'\ensuremath{\supseteq}',
0x2288: r'\ensuremath{\nsubseteq}',
0x2289: r'\ensuremath{\nsupseteq}',
0x228A: r'\ensuremath{\subsetneq}',
0x228B: r'\ensuremath{\supsetneq}',
#...
0x2293: r'\ensuremath{\sqcap}',
0x2294: r'\ensuremath{\sqcup}',
0x2295: r'\ensuremath{\oplus}',
0x2296: r'\ensuremath{\ominus}',
0x2297: r'\ensuremath{\otimes}',
0x2298: r'\ensuremath{\oslash}',
0x2299: r'\ensuremath{\odot}',
# ...
0x22C0: r'\ensuremath{\bigwedge}',
0x22C1: r'\ensuremath{\bigvee}',
0x22C2: r'\ensuremath{\bigcap}',
0x22C3: r'\ensuremath{\bigcup}',
0x22C4: r'\ensuremath{\diamond}',
0x22C5: r'\ensuremath{\cdot}',
0x22C6: r'\ensuremath{\star}',
0x22C7: r'\ensuremath{\divideontimes}',
0x22C8: r'\ensuremath{\bowtie}',
0x22C9: r'\ensuremath{\ltimes}',
0x22CA: r'\ensuremath{\rtimes}',
0x22CB: r'\ensuremath{\leftthreetimes}',
0x22CC: r'\ensuremath{\rightthreetimes}',
# ...
0x22EE: r'\ensuremath{\vdots}',
0x22EF: r'\ensuremath{\cdots}',
0x22F0: r'\ensuremath{\udots}',
0x22F1: r'\ensuremath{\ddots}',
# ...

# Supplemental Mathematical Operators U+2AXX
0x2A7D: r'\ensuremath{\leqslant}',
0x2A7E: r'\ensuremath{\geqslant}',

# CJK Symbols Punktuation (!) U+3000 : for \langle/\rangle
0x3008: r'\ensuremath{\langle}',
0x3009: r'\ensuremath{\rangle}',

# ligatures
0xFB00: r'ff', # LATIN SMALL LIGATURE FF
0xFB01: r'fi', # LATIN SMALL LIGATURE FI
0xFB02: r'fl', # LATIN SMALL LIGATURE FL
0xFB03: r'ffi', # LATIN SMALL LIGATURE FFI
0xFB04: r'ffl', # LATIN SMALL LIGATURE FFL

}






# ------------------------------------------------------------------------------------------------







def utf8tolatex(s, non_ascii_only=False, brackets=True, substitute_bad_chars=False):
    s = unicode(s); # make sure s is unicode
    s = unicodedata.normalize('NFC', s);

    if not s:
        return ""

    result = u""
    for ch in s:
        #log.longdebug("Encoding char %r", ch)
        if (non_ascii_only and ord(ch) < 127):
            result += ch
        else:
            lch = utf82latex.get(ord(ch), None)
            if (lch is not None):
                # add brackets if needed, i.e. if we have a substituting macro.
                # note: in condition, beware, that lch might be of zero length.
                result += (  '{'+lch+'}' if brackets and lch[0:1] == '\\' else
                             lch  )
            elif ((ord(ch) >= 32 and ord(ch) <= 127) or
                  (ch in "\n\r\t")):
                # ordinary printable ascii char, just add it
                result += ch
            else:
                # non-ascii char
                log.warning(u"Character cannot be encoded into LaTeX: U+%04X - `%s'" % (ord(ch), ch))
                if (substitute_bad_chars):
                    result += r'{\bfseries ?}'
                else:
                    # keep unescaped char
                    result += ch

    return result












if __name__ == '__main__':

    try:

        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        log.addHandler(ch)

        import fileinput

        print("Please type some unicode text (Ctrl+D twice to stop) ...")

        latex = ''
        for line in fileinput.input():
            latex += line;

        print('\n--- LATEX ---\n')
        print(utf8tolatex(latex.decode('utf-8')).encode('utf-8'))
        print('\n-------------\n')

    except:
        import pdb;
        import sys;
        print("\nEXCEPTION: " + unicode(sys.exc_info()[1]) + "\n")
        pdb.post_mortem()


