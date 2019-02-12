from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

path = "M -0.20045214,50.310224 c 0.044545,-0.02228 0.086388,-0.05107 0.1336348,-0.06682 0.02113,-0.007 0.046896,0.0099 0.066817,0 0.028173,-0.01408 0.038645,-0.05273 0.066817,-0.06682 0.019921,-0.01 0.046896,0.0099 0.066817,0 0.056345,-0.02817 0.073871,-0.113715 0.1336348,-0.133635 0.042259,-0.01408 0.093793,0.01992 0.1336348,0 0,-0.06912 -0.015749,-0.09235 0.066817,-0.133633 0.019921,-0.0099 0.046896,0.0099 0.066817,0 0.028173,-0.01408 0.038645,-0.05273 0.066817,-0.06682 0.019921,-0.0099 0.046896,0.0099 0.066817,0 0.028173,-0.01408 0.038645,-0.05273 0.066817,-0.06682 0.019921,-0.01 0.045688,0.007 0.066817,0 0.094494,-0.0315 0.1727755,-0.102137 0.2672696,-0.133636 0.02113,-0.007 0.046896,0.0099 0.066817,0 0.028173,-0.01408 0.036936,-0.05686 0.066818,-0.06681 0.042259,-0.01408 0.091376,0.01408 0.1336347,0 0.029881,-0.01 0.036936,-0.05686 0.066817,-0.06682 0.042259,-0.01408 0.091376,0.01408 0.1336347,0 0.029882,-0.0099 0.036936,-0.05686 0.066817,-0.06682 0.042259,-0.01408 0.091376,0.01408 0.133635,0 0.029882,-0.01 0.036935,-0.05686 0.066817,-0.06682 0.042259,-0.01408 0.091376,0.01408 0.1336347,0 0.029882,-0.0099 0.04061,-0.04934 0.066817,-0.06682 0.4844651,-0.242231 -0.1056476,0.07043 0.2004523,-0.133633 0.2271398,-0.151426 0.035834,-0.009 0.2672694,-0.06682 0.048316,-0.01206 0.085319,-0.05474 0.1336347,-0.06682 0.043215,-0.0108 0.091376,0.01407 0.133635,0 0.029881,-0.01 0.040609,-0.04934 0.066817,-0.06682 -0.00761,-0.12658 0.1559073,-0.04455 0.200452,-0.06682 0.028173,-0.01408 0.036936,-0.05686 0.066817,-0.06682 0.060136,-0.02006 0.1403167,0.02005 0.2004523,0 0.047247,-0.01574 0.086388,-0.05107 0.1336347,-0.06682 0.02113,-0.007 0.045688,0.007 0.066817,0 0.047247,-0.01574 0.086388,-0.05107 0.133635,-0.06682 0.02113,-0.007 0.046896,0.01 0.066817,0 0.028173,-0.01408 0.038645,-0.05273 0.066817,-0.06682 0.039842,-0.01992 0.093792,0.01992 0.1336347,0 0.028172,-0.01408 0.038645,-0.05273 0.066817,-0.06682 0.039842,-0.01992 0.1021368,0.0315 0.1336347,0 0.015748,-0.01574 -0.015748,-0.05107 0,-0.06681 0.015748,-0.01574 0.046896,0.0099 0.066818,0 0.028173,-0.01408 0.038645,-0.05273 0.066817,-0.06682 0.039842,-0.01992 0.093793,0.01992 0.1336347,0 0.028173,-0.01408 0.038645,-0.05273 0.066817,-0.06682 0.053454,-0.02673 0.1469982,0.02673 0.2004523,0 0.2216052,-0.221604 -0.062996,0.0315 0.1336347,-0.06682 0.056345,-0.02817 0.07252,-0.118356 0.1336347,-0.133636 0.064822,-0.01619 0.1356299,0.01622 0.2004523,0 0.030557,-0.0076 0.038644,-0.05273 0.066817,-0.06681 0.044282,-0.02215 0.2112682,0.01868 0.2672694,0 0.047247,-0.01574 0.086388,-0.05107 0.1336347,-0.06682 0.02113,-0.007 0.046896,0.0099 0.066818,0 0.3057969,-0.1529 -0.2835341,0.02769 0.200452,-0.133635 0.02113,-0.007 0.046896,0.0099 0.066817,0 0.2037638,-0.101881 -0.1222053,-0.05297 0.2004523,-0.133634 0.043215,-0.0108 0.091376,0.01408 0.1336347,0 0.029882,-0.0099 0.040609,-0.04935 0.066817,-0.06682 0.041438,-0.02763 0.086388,-0.05107 0.1336347,-0.06682 0.02113,-0.007 0.044545,0 0.066817,0 0.044545,0 0.091376,0.01408 0.133635,0 0.029881,-0.01 0.040609,-0.04934 0.066817,-0.06682 0.041438,-0.02763 0.086388,-0.05107 0.1336347,-0.06682 0.02113,-0.007 0.045688,0.007 0.066817,0 0.047247,-0.01574 0.085319,-0.05474 0.1336347,-0.06681 0.043215,-0.0108 0.091376,0.01408 0.1336349,0 0.1203158,-0.04011 0.013319,-0.09353 0.1336347,-0.133636 0.042259,-0.01408 0.091376,0.01408 0.1336347,0 0.029882,-0.01 0.04061,-0.04935 0.066817,-0.06682 0.041438,-0.02763 0.092197,-0.03919 0.133635,-0.06682 0.026207,-0.01746 0.036936,-0.05686 0.066817,-0.06682 0.042259,-0.01407 0.091376,0.01408 0.1336347,0 0.029882,-0.0099 0.038645,-0.05273 0.066817,-0.06681 0.01992,-0.01 0.045688,0.007 0.066817,0 0.047247,-0.01574 0.085319,-0.05474 0.133635,-0.06682 0.043215,-0.01079 0.091376,0.01408 0.1336347,0 0.029882,-0.0099 0.036936,-0.05686 0.066817,-0.06682 0.084518,-0.02817 0.1808399,0.02162 0.2672699,0 0.04832,-0.01206 0.08639,-0.05107 0.133634,-0.06682 0.05378,-0.01791 0.224572,0.02135 0.26727,0 0.02817,-0.01408 0.03694,-0.05686 0.06682,-0.06682 0.04226,-0.01408 0.08909,0 0.133635,0 0.02227,0 0.0469,0.01 0.06682,0 0.221606,-0.221605 -0.063,0.0315 0.133635,-0.06682 0.02817,-0.01407 0.03865,-0.05273 0.06682,-0.06682 0.01992,-0.0099 0.0469,0.0099 0.06682,0 0.02817,-0.01408 0.03865,-0.05273 0.06682,-0.06682 0.01992,-0.0099 0.0469,0.01 0.06682,0 0.05635,-0.02817 0.08122,-0.09869 0.133634,-0.133636 0.04144,-0.02763 0.0922,-0.03919 0.133635,-0.06681 0.05242,-0.03495 0.07729,-0.105463 0.133635,-0.133636 0.01992,-0.0099 0.0469,0.01 0.06682,0 0.02817,-0.01408 0.03864,-0.05273 0.06682,-0.06682 0.01992,-0.01 0.0469,0.0099 0.06682,0 0.305797,-0.152897 -0.283534,0.02769 0.200452,-0.133636 0.02113,-0.007 0.0469,0.01 0.06682,0 0.05635,-0.02817 0.07387,-0.113712 0.133634,-0.133633 0.04226,-0.01408 0.09138,0.01408 0.133635,0 0.05976,-0.01992 0.08122,-0.09869 0.133635,-0.133636 0.04144,-0.02762 0.0922,-0.03919 0.133635,-0.06682 0.05632,-0.03754 0.226444,-0.253659 0.267269,-0.267269 0.04226,-0.01408 0.09138,0.01408 0.133635,0 0.02988,-0.0099 0.04454,-0.04454 0.06682,-0.06682 0.04454,-0.02228 0.08532,-0.05474 0.133635,-0.06682 0.04322,-0.0108 0.09042,0.0108 0.133635,0 0.09663,-0.02416 0.170638,-0.109477 0.267269,-0.133633 0.04322,-0.0108 0.09042,0.0108 0.133635,0 0.09663,-0.02416 0.170638,-0.109477 0.26727,-0.133636 0.04322,-0.0108 0.09042,0.01079 0.133634,0 0.132692,-0.03317 0.268213,-0.167277 0.400905,-0.200451 0.04322,-0.0108 0.09042,0.0108 0.133634,0 0.04832,-0.01206 0.08532,-0.05474 0.133635,-0.06682 0.04322,-0.01079 0.09042,0.0108 0.133635,0 0.09663,-0.02416 0.170638,-0.109476 0.26727,-0.133635 0.04321,-0.0108 0.09042,0.0108 0.133634,0 0.04832,-0.01209 0.08532,-0.05474 0.133635,-0.06682 0.04322,-0.0108 0.09042,0.01079 0.133635,0 0.09663,-0.02416 0.170638,-0.109479 0.267269,-0.133635 0.475954,-0.118989 -0.338515,0.202223 0.334087,-0.06682 0.09248,-0.03699 0.170638,-0.109477 0.26727,-0.133636 0.475953,-0.118986 -0.338515,0.202224 0.334087,-0.06681 0.0092,-0.0037 0.264118,-0.133006 0.267269,-0.133636 0.06552,-0.0131 0.134932,0.0131 0.200452,0 0.09767,-0.01953 0.170638,-0.109477 0.26727,-0.133636 0.04322,-0.0108 0.09042,0.0108 0.133635,0 0.09663,-0.02416 0.170638,-0.109476 0.267269,-0.133633 0.04322,-0.01079 0.09042,0.0108 0.133635,0 0.09663,-0.02416 0.170638,-0.109476 0.267269,-0.133636 0.04322,-0.0108 0.09042,0.0108 0.133635,0 0.04832,-0.01209 0.08909,-0.04454 0.133635,-0.06682 0.06682,-0.02228 0.131388,-0.053 0.200452,-0.06682 0.04368,-0.0087 0.09042,0.0108 0.133635,0 0.09663,-0.02416 0.170638,-0.109479 0.267269,-0.133635 0.475954,-0.118989 -0.338515,0.202223 0.334087,-0.06682 0.302791,-0.121116 0.0093,-0.0062 0.200452,-0.133636 0.08288,-0.05525 0.187586,-0.07387 0.26727,-0.133633 0.0504,-0.0378 0.08909,-0.08909 0.133635,-0.133636 0.02227,-0.02228 0.03864,-0.05273 0.06682,-0.06682 0.50788,-0.253939 0.03948,-0.0099 0.26727,-0.06682 0.134178,0.01535 0.217727,-0.104545 0.334086,-0.133636 0.04322,-0.0108 0.09138,0.01408 0.133635,0 0.02988,-0.01 0.03694,-0.05686 0.06682,-0.06682 0.04226,-0.01407 0.09042,0.0108 0.133634,0 0.09663,-0.02416 0.170638,-0.109476 0.26727,-0.133633 0.04322,-0.0108 0.08995,0.0087 0.133635,0 0.06906,-0.01381 0.133634,-0.04454 0.200452,-0.06682 0.06682,-0.02228 0.135058,-0.04066 0.200452,-0.06682 0.17818,-0.07127 0.112482,-0.08931 0.334087,-0.133635 0.356965,-0.07139 -0.150378,0.126968 0.334087,-0.06682 0.0092,-0.0037 0.264118,-0.133004 0.267269,-0.133633 0.06552,-0.0131 0.134544,0.01098 0.200452,0 0.06947,-0.01159 0.131389,-0.053 0.200453,-0.06682 0.04368,-0.0087 0.08995,0.0087 0.133634,0 0.06906,-0.01381 0.130979,-0.05524 0.200452,-0.06682 0.06591,-0.01098 0.134933,0.0131 0.200453,0 0.0032,-5.29e-4 0.258032,-0.129939 0.267269,-0.133633 0.06539,-0.02617 0.133635,-0.04454 0.200452,-0.06682 0.06682,-0.02228 0.132124,-0.04974 0.200452,-0.06682 0.02161,-0.0054 0.04454,0 0.06682,0 0.06682,-0.02228 0.135058,-0.04066 0.200452,-0.06682 0.09248,-0.03699 0.170638,-0.109476 0.26727,-0.133635 0.305796,-0.07645 -0.06948,0.134964 0.334087,-0.06682 0.02817,-0.01408 0.04162,-0.04792 0.06682,-0.06682 0.08964,-0.06723 0.223046,-0.156035 0.334087,-0.200453 0.06539,-0.02617 0.135058,-0.04066 0.200452,-0.06681 0.138243,-0.0553 0.262661,-0.145156 0.400904,-0.200454 0.06539,-0.02617 0.135058,-0.04066 0.200452,-0.06682 0.04624,-0.01849 0.0874,-0.04832 0.133636,-0.06681 0.06539,-0.02617 0.140057,-0.03058 0.200451,-0.06682 0.05402,-0.03241 0.07962,-0.101224 0.133636,-0.133636 0.288258,-0.172955 0.101213,-0.0086 0.334086,-0.06682 0.04832,-0.01209 0.0874,-0.04832 0.133634,-0.06682 0.06539,-0.02617 0.133635,-0.04454 0.200453,-0.06682 0.06682,-0.02228 0.13098,-0.05524 0.200451,-0.06682 0.639461,0 -0.149407,0.02988 0.334087,-0.06682 0.13104,-0.02622 0.269089,0.02196 0.400904,0 0.138949,-0.02315 0.261959,-0.110477 0.400905,-0.133636 0.06591,-0.01098 0.134543,0.01098 0.200454,0 0.06947,-0.01159 0.133633,-0.04454 0.200451,-0.06681 0.133635,-0.04455 0.267269,-0.08909 0.400904,-0.133636 0.06682,-0.02228 0.130728,-0.05686 0.200451,-0.06682 0.0882,-0.01259 0.179393,0.01466 0.267272,0 0.04913,-0.0082 0.08739,-0.04832 0.133633,-0.06682 0.06539,-0.02617 0.135059,-0.04066 0.200453,-0.06682 0.04624,-0.01849 0.08739,-0.04832 0.133634,-0.06682 0.06539,-0.02617 0.135059,-0.04066 0.200453,-0.06682 0.04624,-0.01849 0.0848,-0.05705 0.133633,-0.06682 0.06552,-0.0131 0.134933,0.0131 0.200454,0 0.04883,-0.0098 0.08739,-0.04832 0.133633,-0.06682 0.06539,-0.02617 0.135059,-0.04066 0.200454,-0.06682 0.04624,-0.01849 0.08532,-0.05474 0.133633,-0.06681 0.04322,-0.0108 0.09042,0.01079 0.133635,0 0.04832,-0.01209 0.0874,-0.04832 0.133636,-0.06682 0.06539,-0.02617 0.133633,-0.04454 0.200451,-0.06682 0.06682,-0.02228 0.13139,-0.053 0.200454,-0.06682 0.04368,-0.0087 0.09042,0.0108 0.133633,0 0.04832,-0.01206 0.0848,-0.05705 0.133636,-0.06682 0.06552,-0.0131 0.134932,0.0131 0.200451,0 0.04884,-0.0098 0.08909,-0.04454 0.133635,-0.06682 0.06682,-0.02228 0.131387,-0.05301 0.200451,-0.06682 0.04368,-0.0087 0.08996,0.0087 0.133636,0 0.06906,-0.01381 0.130979,-0.05524 0.200451,-0.06682 0.06591,-0.01098 0.134546,0.01098 0.200454,0 0.06947,-0.01159 0.130979,-0.05524 0.200451,-0.06682 0.181353,-0.03023 0.420005,0.03023 0.601358,0 0.06947,-0.01159 0.131387,-0.053 0.200451,-0.06682 0.04368,-0.0087 0.08996,0.0087 0.133636,0 0.06906,-0.01381 0.130979,-0.05524 0.200451,-0.06681 0.131818,-0.02196 0.269864,0.02622 0.400904,0 0.04884,-0.0098 0.0848,-0.05705 0.133636,-0.06682 0.156951,-0.03139 0.444405,0.03139 0.601356,0 0.04884,-0.0098 0.08451,-0.05863 0.133635,-0.06682 0.08788,-0.01466 0.179076,0.01259 0.267269,0 0.06972,-0.01 0.130979,-0.05524 0.200451,-0.06682 0.06591,-0.01098 0.134546,0.01098 0.200454,0 0.06947,-0.01159 0.133633,-0.04454 0.200451,-0.06682 0.133635,-0.04454 0.270116,-0.08132 0.400904,-0.133633 0.04624,-0.01849 0.0874,-0.04832 0.133636,-0.06682 0.0654,-0.02617 0.133633,-0.04454 0.200451,-0.06682 0.06682,-0.02228 0.130979,-0.05524 0.200454,-0.06682 0.06591,-0.01098 0.134932,0.0131 0.200451,0 0.04884,-0.0098 0.0848,-0.05705 0.133635,-0.06682 0.06552,-0.0131 0.134544,0.01098 0.200451,0 0.06947,-0.01159 0.13139,-0.053 0.200454,-0.06682 0.04368,-0.0087 0.08995,0.0087 0.133633,0 0.06906,-0.01381 0.135059,-0.04066 0.200454,-0.06682 0.04624,-0.0185 0.0848,-0.05705 0.133633,-0.06682 0.06552,-0.0131 0.135631,0.01622 0.200453,0 0.03056,-0.0076 0.04455,-0.04455 0.06682,-0.06682 0.06682,-0.02228 0.131387,-0.053 0.200451,-0.06682 0.04368,-0.0087 0.08996,0.0087 0.133636,0 0.135948,0.0232 0.216474,-0.110112 0.334087,-0.133633 0.06552,-0.0131 0.134932,0.0131 0.200451,0 0.09767,-0.01953 0.169598,-0.114102 0.267269,-0.133636 0.509727,0 -0.05271,0.02988 0.334086,-0.06682 0.108038,-0.02701 0.224888,0.02183 0.334087,0 0.04884,-0.0098 0.0848,-0.05705 0.133636,-0.06682 0.06552,-0.0131 0.134543,0.01098 0.200453,0 0.138946,-0.02315 0.262777,-0.106008 0.400902,-0.133633 0.04368,-0.0087 0.08996,0.0087 0.133636,0 0.138129,-0.02763 0.261959,-0.110477 0.400905,-0.133635 0.06591,-0.01098 0.134543,0.01098 0.200451,0 0.06947,-0.01159 0.130979,-0.05524 0.200453,-0.06682 0.06591,-0.01098 0.134933,0.0131 0.200451,0 0.04884,-0.0098 0.0848,-0.05705 0.133636,-0.06682 0.06552,-0.0131 0.134543,0.01098 0.200451,0 0.06947,-0.01159 0.131389,-0.05301 0.200454,-0.06682 0.04368,-0.0087 0.08995,0.0087 0.133633,0 0.06906,-0.01381 0.133636,-0.04455 0.200453,-0.06682 0.06682,-0.02228 0.135057,-0.04066 0.200451,-0.06682 0.178181,-0.07127 0.112483,-0.08931 0.334087,-0.133636 0.04368,-0.0087 0.08996,0.0087 0.133636,0 0.06906,-0.01381 0.135056,-0.04066 0.200451,-0.06681 0.04624,-0.0185 0.0848,-0.05705 0.133636,-0.06682 0.109198,-0.02183 0.224887,0.02183 0.334086,0 0.06906,-0.01381 0.13139,-0.053 0.200454,-0.06682 0.356963,-0.07139 -0.150379,0.126968 0.334087,-0.06682 0.04624,-0.01849 0.0848,-0.05705 0.133633,-0.06682 0.06552,-0.0131 0.134932,0.0131 0.200453,0 0.04883,-0.0098 0.08451,-0.05863 0.133633,-0.06681 0.08788,-0.01466 0.179393,0.01466 0.267272,0 0.04912,-0.0082 0.08451,-0.05863 0.133633,-0.06682 0.08788,-0.01466 0.179075,0.01259 0.267269,0 0.06973,-0.01 0.130979,-0.05524 0.200454,-0.06682 0.18135,-0.03023 0.420004,0.03023 0.601355,0 0.06947,-0.01159 0.130979,-0.05524 0.200454,-0.06682 0.06591,-0.01098 0.134543,0.01098 0.200451,0 0.06947,-0.01159 0.130979,-0.05524 0.200453,-0.06682 0.131816,-0.02196 0.269865,0.02622 0.400902,0 0.04884,-0.0098 0.0848,-0.05705 0.133636,-0.06682 0.06552,-0.0131 0.133636,0 0.200451,0 0.11403,0 0.516258,0.01418 0.601358,0 0.04912,-0.0082 0.0874,-0.04832 0.133633,-0.06682 0.0654,-0.02617 0.13139,-0.05301 0.200454,-0.06682 0.356965,-0.07139 -0.150379,0.126968 0.334087,-0.06682 0.155794,-0.06232 0.144139,-0.101976 0.334086,-0.133636 0.06591,-0.01098 0.134933,0.0131 0.200451,0 0.04884,-0.0098 0.08532,-0.05474 0.133636,-0.06681 0.04322,-0.0108 0.08996,0.0087 0.133636,0 0.06906,-0.01381 0.131387,-0.05301 0.200451,-0.06682 0.04368,-0.0087 0.08909,0 0.133636,0 0.06682,0 0.134932,0.0131 0.200451,0 0.04884,-0.0098 0.0848,-0.05705 0.133635,-0.06682 0.06552,-0.0131 0.134544,0.01098 0.200451,0 0.06948,-0.01159 0.13098,-0.05524 0.200454,-0.06682 0.06591,-0.01098 0.134932,0.0131 0.200451,0 0.04884,-0.0098 0.0848,-0.05705 0.133636,-0.06682 0.639461,0 -0.149408,0.02988 0.334086,-0.06681 0.171326,-0.03427 0.363212,0.03426 0.534538,0 0.04884,-0.0098 0.08532,-0.05474 0.133636,-0.06682 0.04321,-0.0108 0.08909,0 0.133636,0 0.06681,0 0.133633,0 0.200451,0 0.04454,0 0.08996,0.0087 0.133635,0 0.138129,-0.02763 0.261956,-0.110477 0.400905,-0.133636 0.131815,-0.02196 0.269086,0.02196 0.400902,0 0.06947,-0.01159 0.130979,-0.05524 0.200453,-0.06682 0.06591,-0.01098 0.134544,0.01098 0.200451,0 0.06948,-0.01159 0.133636,-0.04455 0.200454,-0.06682 0.06682,-0.02228 0.135057,-0.04066 0.200451,-0.06682 0.155795,-0.06232 0.14414,-0.101978 0.334087,-0.133635 0.06591,-0.01098 0.134546,0.01098 0.200453,0 0.06947,-0.01159 0.13098,-0.05524 0.200451,-0.06682 0.06591,-0.01098 0.134544,0.01098 0.200454,0 0.138946,-0.02315 0.261956,-0.110477 0.400902,-0.133633 0.06591,-0.01098 0.134546,0.01098 0.200454,0 0.06947,-0.01159 0.130728,-0.05686 0.200451,-0.06682 0.0882,-0.01259 0.178181,0 0.267271,0 0.155906,0 0.311814,0 0.46772,0 0.155908,0 0.311814,0 0.467722,0 0.06682,0 0.134305,0.0094 0.200451,0 0.09091,-0.01299 0.176149,-0.05543 0.267272,-0.06682 0.0884,-0.01106 0.178178,0 0.267269,0 0.178178,0 0.356359,0 0.534537,0 0.08909,0 0.178869,0.01106 0.267272,0 0.09112,-0.0114 0.176146,-0.05543 0.267269,-0.06682 0.218995,-0.02737 0.519385,0.0308 0.734991,0 0.06972,-0.0099 0.130728,-0.05686 0.200451,-0.06682 0.154342,-0.02204 0.313383,0.02204 0.467722,0 0.09091,-0.01299 0.176361,-0.05383 0.267269,-0.06681 0.06615,-0.0094 0.134308,0.0094 0.200454,0 0.09091,-0.01299 0.176361,-0.05383 0.267269,-0.06682 0.06615,-0.0094 0.134543,0.01098 0.200451,0 0.06947,-0.01159 0.130979,-0.05524 0.200453,-0.06682 0.06591,-0.01098 0.134544,0.01098 0.200451,0 0.06948,-0.01159 0.13098,-0.05524 0.200454,-0.06682 0.06591,-0.01098 0.133633,0 0.200451,0 0.267269,0 0.53454,0 0.801809,0 0.06682,0 0.133636,0 0.200451,0 0.06682,0 0.134546,0.01098 0.200454,0 0.06947,-0.01159 0.130979,-0.05524 0.200451,-0.06682 0.06591,-0.01098 0.133636,0 0.200453,0 0.08909,0 0.178179,0 0.267269,0 0.400905,0 0.801809,0 1.202714,0 0.111361,0 0.222724,0 0.334087,0 0.06682,0 0.134543,0.01098 0.200451,0 0.06947,-0.01159 0.130979,-0.05524 0.200453,-0.06682 0.06591,-0.01098 0.134544,0.01098 0.200451,0 0.138946,-0.02315 0.262777,-0.106008 0.400905,-0.133633 0.04368,-0.0087 0.08996,0.0087 0.133636,0 0.135948,0.0232 0.216474,-0.110112 0.334086,-0.133636 0.108117,-0.03276 0.224886,0.02183 0.334087,0 0.138129,-0.02762 0.262776,-0.106008 0.400905,-0.133633 0.04368,-0.0087 0.08995,0.0087 0.133633,0 0.138128,-0.02763 0.261958,-0.110477 0.400904,-0.133636 0.06591,-0.01098 0.134933,0.0131 0.200454,0 0.04883,-0.0098 0.0848,-0.05705 0.133633,-0.06682 0.108119,-0.03276 0.224888,0.02183 0.334087,0 0.06906,-0.01381 0.131389,-0.053 0.200454,-0.06682 0.04368,-0.0087 0.08995,0.0087 0.133633,0 0.13595,0.0232 0.216476,-0.110111 0.334086,-0.133633 0.131041,-0.02622 0.269865,0.02619 0.400905,0 0.04884,-0.0098 0.0848,-0.05705 0.133636,-0.06682 0.06552,-0.0131 0.133633,0 0.200451,0 0.06682,0 0.133635,0 0.200453,0 0.04455,0 0.09042,0.01079 0.133633,0 0.04832,-0.01206 0.0848,-0.05705 0.133636,-0.06682 0.152879,-0.03057 0.313936,0.02564 0.467723,0 0.04913,-0.0082 0.08451,-0.05863 0.133633,-0.06682 0.153786,-0.02564 0.313936,0.02564 0.467722,0 0.06947,-0.01159 0.13139,-0.053 0.200451,-0.06682 0.109202,-0.02183 0.224242,0.01831 0.33409,0 0.06947,-0.01159 0.130976,-0.05524 0.200451,-0.06682 0.06591,-0.01098 0.134932,0.0131 0.20045,0 0.04884,-0.0098 0.0848,-0.05705 0.133636,-0.06682 0.06552,-0.0131 0.134543,0.01098 0.200451,0 0.06947,-0.01159 0.13098,-0.05524 0.200454,-0.06682 0.109847,-0.01831 0.224239,0.01831 0.334087,0 0.172418,0.0691 0.262776,-0.106008 0.400904,-0.133636 0.13104,-0.02622 0.269087,0.02196 0.400905,0 0.138946,-0.02315 0.261956,-0.110477 0.400904,-0.133633 0.131816,-0.02196 0.269087,0.02196 0.400905,0 0.06947,-0.01159 0.130977,-0.05524 0.200451,-0.06682 0.06591,-0.01098 0.134543,0.01098 0.200451,0 0.06947,-0.01159 0.130979,-0.05524 0.200454,-0.06682 0.06591,-0.01098 0.134305,0.0094 0.200451,0 0.09091,-0.01299 0.17636,-0.05383 0.267271,-0.06682 0.06615,-0.0094 0.134543,0.01098 0.200451,0 0.06947,-0.01159 0.130979,-0.05524 0.200451,-0.06682 0.06591,-0.01098 0.134546,0.01098 0.200454,0 0.06947,-0.01159 0.130979,-0.05524 0.200451,-0.06682 0.06591,-0.01098 0.133635,0 0.200453,0 0.06682,0 0.133633,0 0.200451,0 0.04454,0 0.08996,0.0087 0.133636,0 0.06906,-0.01381 0.131387,-0.05301 0.200451,-0.06682 0.04368,-0.0087 0.08996,0.0087 0.133636,0 0.565367,-0.188457 -0.07405,0.0013 0.334086,-0.06682 0.09058,-0.01511 0.178972,-0.04159 0.267269,-0.06682 0.06772,-0.01934 0.130728,-0.05686 0.200454,-0.06682 0.08819,-0.0126 0.178723,0.0098 0.267269,0 0.112874,-0.01254 0.221213,-0.05427 0.334086,-0.06682 0.154954,-0.01722 0.311814,0 0.467723,0 0.267269,0 0.534538,0 0.801806,0 0.178181,0 0.35636,0 0.534541,0 0.04454,0 0.08995,0.0087 0.133636,0 0.135948,0.0232 0.216474,-0.110114 0.334086,-0.133635 0.06552,-0.0131 0.134932,0.0131 0.200451,0 0.04884,-0.0098 0.08909,-0.04455 0.133636,-0.06682 0.08909,-0.04455 0.174786,-0.09664 0.267269,-0.133633 0.06539,-0.02617 0.135056,-0.04066 0.200451,-0.06682 0.04624,-0.0185 0.08739,-0.04832 0.133636,-0.06682 0.06539,-0.02617 0.140057,-0.03058 0.200451,-0.06682 0.05402,-0.03241 0.07515,-0.110239 0.133635,-0.133636 0.06204,-0.02482 0.134932,0.0131 0.200454,0 0.04883,-0.0098 0.08909,-0.04454 0.133633,-0.06681 0.08909,-0.04454 0.174789,-0.09664 0.267269,-0.133636 0.06539,-0.02617 0.133636,-0.04454 0.200453,-0.06682 0.06682,-0.02228 0.13098,-0.05524 0.200451,-0.06682 0.06591,-0.01098 0.134546,0.01098 0.200454,0 0.06947,-0.01159 0.130979,-0.05524 0.200451,-0.06681 0.06591,-0.01098 0.134543,0.01098 0.200454,0 0.06947,-0.01159 0.130976,-0.05524 0.200451,-0.06682 0.06591,-0.01098 0.134543,0.01098 0.200453,0 0.06947,-0.01159 0.130019,-0.06682 0.200451,-0.06682 0.07043,0 0.13098,0.05524 0.200451,0.06682 0.02698,0.129736 0.307113,-0.06682 0.334087,-0.06682 0.07043,0 0.130979,0.05524 0.200454,0.06682 0.06591,0.01098 0.133635,0 0.200451,0 0.06682,0 0.133635,0 0.200453,0 0.267269,0 0.534538,0 0.801809,0 0.06682,0 0.133633,0 0.200451,0 0.06682,0 0.134544,-0.01098 0.200451,0 0.06948,0.01159 0.13139,0.053 0.200454,0.06682 0.04368,0.0087 0.08909,0 0.133633,0 0.06682,0 0.133636,0 0.200454,0 0.111363,0 0.222723,0 0.334086,0 0.02228,0 0.04521,0.0054 0.06682,0 0.06833,-0.01709 0.132123,-0.04974 0.200451,-0.06682 0.02162,-0.0054 0.04454,0 0.06682,0 0.06682,0 0.133636,0 0.200454,0 0.04454,0 0.08995,0.0087 0.133633,0 0.06906,-0.01381 0.131389,-0.053 0.200453,-0.06682 0.04368,-0.0087 0.08909,0 0.133634,0 0.06682,0 0.133635,0 0.200453,0 0.200451,0 0.400905,0 0.601356,0 0.155908,0 0.311814,0 0.467722,0 0.06681,0 0.133633,0 0.200451,0 0.04454,0 0.09042,-0.0108 0.133636,0 0.04832,0.01206 0.08532,0.05474 0.133633,0.06682 0.04322,0.0108 0.08996,-0.0087 0.133636,0 0.06906,0.01381 0.130979,0.05524 0.200451,0.06682 0.06591,0.01098 0.133636,0 0.200453,0 0.06682,0 0.133634,0 0.200451,0 0.222727,0 0.44545,0 0.668174,0 0.289544,0 0.579085,0 0.868627,0 0.09663,0 0.397163,0.0141 0.467722,0 0.04883,-0.0098 0.08532,-0.05474 0.133633,-0.06682 0.108038,-0.02701 0.224888,0.02183 0.334087,0 0.04884,-0.0098 0.08532,-0.05474 0.133636,-0.06682 0.08643,-0.02162 0.179909,0.01746 0.267269,0 0.06906,-0.01381 0.131389,-0.053 0.200453,-0.06682 0.04368,-0.0087 0.08909,0 0.133634,0 0.111363,0 0.222726,0 0.334086,0 0.311817,0 0.623631,0 0.935445,0 0.200451,0 0.400905,0 0.601356,0 0.06682,0 0.133636,0 0.200453,0 0.04454,0 0.09042,0.01079 0.133634,0 0.04832,-0.01206 0.08532,-0.05474 0.133635,-0.06682 0.04322,-0.01079 0.08909,0 0.133633,0 0.155909,0 0.311817,0 0.467723,0 0.222726,0 0.44545,0 0.66818,0 0.0445,0 0.0891,0 0.13363,0 0.0446,0 0.0904,0.0108 0.13364,0 0.0483,-0.01206 0.0848,-0.05705 0.13363,-0.06681 0.0655,-0.0131 0.13364,0 0.20046,0 0.0668,0 0.13363,0 0.20045,0 0.0445,0 0.09,0.0087 0.13363,0 0.0691,-0.01381 0.13098,-0.05524 0.20045,-0.06682 0.0659,-0.01098 0.13364,0 0.20046,0 0.0668,-0.02228 0.13138,-0.05301 0.20045,-0.06682 0.0874,-0.01746 0.17818,0 0.26727,0 0.15591,0 0.31181,0 0.46772,0 0.0446,0 0.0904,0.01079 0.13364,0 0.0483,-0.01207 0.0848,-0.05705 0.13363,-0.06682 0.0655,-0.0131 0.13493,0.0131 0.20045,0 0.0488,-0.0098 0.0853,-0.05474 0.13364,-0.06682 0.0432,-0.01079 0.09,0.0087 0.13363,0 0.0691,-0.01381 0.13139,-0.053 0.20045,-0.06682 0.0874,-0.01746 0.18084,0.02162 0.26727,0 0.0483,-0.01206 0.0853,-0.05474 0.13364,-0.06682 0.0526,-0.01315 0.33142,0 0.4009,0 0.0446,0 0.0904,0.0108 0.13364,0 0.0483,-0.01209 0.0853,-0.05474 0.13363,-0.06682 0.0879,-0.02196 0.25111,0.02766 0.33409,0 0.0299,-0.0099 0.0369,-0.05686 0.0668,-0.06682 0.0422,-0.01408 0.0891,0 0.13363,0 0.0573,0 0.36181,0.01304 0.40091,0 0.0299,-0.0099 0.0369,-0.05686 0.0668,-0.06682 0.0391,-0.01304 0.34355,0 0.40091,0 0.0223,0 0.0457,0.007 0.0668,0 0.0472,-0.01574 0.0853,-0.05474 0.13364,-0.06682 0.0432,-0.0108 0.0891,0 0.13363,0 0.11137,0 0.22273,0 0.33409,0 0.0445,0 0.0914,0.01408 0.13363,0 0.0299,-0.0099 0.0387,-0.05273 0.0668,-0.06682 0.0199,-0.0099 0.0446,0 0.0668,0 0.0223,0 0.0446,0 0.0668,0 0.11136,0 0.22272,0 0.33408,0 0.0446,0 0.0891,0 0.13364,0 0.0223,0 0.0457,0.007 0.0668,0 0.0472,-0.01574 0.0853,-0.05474 0.13363,-0.06682 0.0648,-0.01622 0.13363,0 0.20045,0 0.31182,0 0.62363,0 0.93545,0 0.0547,0 0.29079,-0.01442 0.33408,0 0.37857,0.189283 -0.0996,-0.0249 0.26727,0.06682 0.0483,0.01209 0.0853,0.05474 0.13364,0.06682 0.0864,0.02162 0.18084,-0.02162 0.26727,0 0.0483,0.01209 0.0853,0.05474 0.13363,0.06682 0.0864,0.02162 0.18275,-0.02817 0.26727,0 0.0299,0.0099 0.0369,0.05686 0.0668,0.06682 0.0423,0.01408 0.0891,0 0.13363,0 0.11137,0 0.22273,0 0.33409,0 0.49,0 0.97999,0 1.46998,0 0.15591,0 0.31182,0 0.46773,0 0.0445,0 0.0914,-0.01408 0.13363,0 0.0299,0.0099 0.0369,0.05686 0.0668,0.06682 0.0423,0.01408 0.0891,0 0.13363,0 0.11136,0 0.22273,0 0.33409,0 0.0445,0 0.0904,-0.0108 0.13363,0 0.0483,0.01206 0.0864,0.05107 0.13364,0.06682 0.0211,0.007 0.0445,0 0.0668,0 0.0891,0 0.17818,0 0.26726,0 0.13364,0 0.26728,0 0.40091,0 0.0445,0 0.0914,0.01408 0.13363,0 0.0473,-0.01574 0.0864,-0.05107 0.13364,-0.06682 0.0211,-0.007 0.0445,0 0.0668,0 0.0373,0 0.3035,0.01019 0.33408,0 0.0299,-0.0099 0.0387,-0.05273 0.0668,-0.06682 0.0199,-0.0099 0.0446,0 0.0668,0 0.0223,-0.02228 0.0386,-0.05273 0.0668,-0.06682 0.0199,-0.0099 0.0445,0 0.0668,0 0.0446,0 0.0891,0 0.13364,0 0.20045,0 0.4009,0 0.60135,0 0.0349,0 0.2497,0.0088 0.26727,0 0.0282,-0.01408 0.0369,-0.05686 0.0668,-0.06682 0.0455,-0.01516 0.29866,0.01773 0.33409,0 0.0282,-0.01408 0.0353,-0.06682 0.0668,-0.06682 0.0315,0 0.0353,0.06682 0.0668,0.06682 0.0315,0 0.0387,-0.05273 0.0668,-0.06682 0.0434,-0.0217 0.2917,0.02119 0.33409,0 0.0282,-0.01408 0.0369,-0.05686 0.0668,-0.06682 0.0306,-0.01019 0.2968,0 0.33409,0 0.0223,0 0.0457,0.007 0.0668,0 0.0473,-0.01574 0.0864,-0.05107 0.13363,-0.06682 0.0423,-0.01407 0.0891,0 0.13364,0 0.15591,0 0.31181,0 0.46772,0 0.0446,0 0.0891,0 0.13363,0 0.0446,0 0.0904,0.0108 0.13364,0 0.0483,-0.01209 0.0848,-0.05705 0.13363,-0.06682 0.1092,-0.02183 0.22273,0 0.33409,0 0.0446,0 0.0891,0 0.13363,0 0.0446,0 0.0904,-0.01079 0.13364,0 0.0483,0.01206 0.0838,0.06682 0.13364,0.06682 0.0498,0 0.0838,-0.06682 0.13363,-0.06682 0.0498,0 0.0838,0.06682 0.13363,0.06682 0.31535,0 -0.0431,-0.144399 0.26727,-0.06682 0.0483,0.01206 0.0853,0.05474 0.13364,0.06682 0.0432,0.0108 0.0891,0 0.13363,0 0.0446,0 0.0891,0 0.13364,0 0.17818,0 0.35636,0 0.53454,0 0.0668,0 0.13563,0.01622 0.20045,0 0.0306,-0.0076 0.0445,-0.04454 0.0668,-0.06682 0.0445,-0.02228 0.0848,-0.05705 0.13363,-0.06682 0.0668,0 0.13364,0 0.20045,0 0.0223,-0.02228 0.0369,-0.05686 0.0668,-0.06682 0.23275,-0.07758 0.0387,0.06682 0.26727,0.06682 0.0498,0 0.0853,-0.05474 0.13364,-0.06682 0.0648,-0.01622 0.13363,0 0.20045,0 0.13363,0 0.26727,0 0.4009,0 0.0446,0 0.0904,0.0108 0.13364,0 0.0483,-0.01209 0.0853,-0.05474 0.13363,-0.06682 0.10481,-0.02619 0.22928,0.02619 0.33409,0 0.0483,-0.01209 0.0853,-0.05474 0.13363,-0.06682 0.10804,-0.02701 0.22489,0.02183 0.33409,0 0.0488,-0.0098 0.0853,-0.05474 0.13364,-0.06682 0.0526,-0.01315 0.33141,0 0.4009,0 0.0668,0 0.13363,0 0.20045,0 0.0446,0 0.0904,-0.01079 0.13363,0 0.0483,0.01206 0.0848,0.05705 0.13364,0.06682 0.0655,0.0131 0.13364,0 0.20045,0 0.13364,0 0.26727,0 0.40091,0 0.0445,0 0.0904,-0.0108 0.13363,0 0.0483,0.01209 0.0848,0.05705 0.13364,0.06682 0.0655,0.0131 0.13363,0 0.20045,0 0.0668,0 0.13563,0.01619 0.20045,0 0.0483,-0.01209 0.0838,-0.06682 0.13364,-0.06682 0.0704,0 0.13002,0.06682 0.20045,0.06682 0.0498,0 0.0838,-0.06682 0.13363,-0.06682 0.0498,0 0.0853,0.05474 0.13364,0.06682 0.0432,0.0108 0.0891,0 0.13363,0 0.0668,0 0.13364,0 0.20045,0 0.0223,0 0.0452,-0.0054 0.0668,0 0.0683,0.01709 0.13212,0.04973 0.20045,0.06682 0.0216,0.0054 0.0457,-0.007 0.0668,0 0.0473,0.01574 0.0853,0.05474 0.13364,0.06682 0.0432,0.01079 0.0891,0 0.13363,0 0.0668,0 0.13364,0 0.20045,0 0.0223,0 0.0457,-0.007 0.0668,0 0.0472,0.01574 0.0853,0.05474 0.13363,0.06682 0.0432,0.0108 0.0891,0 0.13364,0 0.0559,0 0.28327,-0.0127 0.33409,0 0.0483,0.01206 0.0848,0.05705 0.13363,0.06682 0.067,0.01339 0.3139,0 0.4009,0 0.0446,0 0.09,-0.0087 0.13364,0 0.0691,0.01381 0.13139,0.053 0.20045,0.06682 0.0874,0.01746 0.18084,-0.02162 0.26727,0 0.0483,0.01206 0.0853,0.05474 0.13364,0.06682 0.0432,0.0108 0.0891,0 0.13363,0 0.13364,0 0.26727,0 0.40091,0 0.0891,0 0.17817,0 0.26727,0 0.0445,0 0.0891,0 0.13363,0 0.0223,0 0.0457,0.007 0.0668,0 0.0473,-0.01574 0.0864,-0.05107 0.13363,-0.06682 0.0433,-0.01442 0.27939,0 0.33409,0 0.13363,0 0.26727,0 0.4009,0 0.0445,0 0.0891,0 0.13364,0 0.0445,0 0.0904,0.01079 0.13363,0 0.0483,-0.01206 0.0853,-0.05474 0.13364,-0.06682 0.25326,-0.06331 0.0398,0.01328 0.20045,0.06682 0.0423,0.01408 0.0891,0 0.13363,0 0.0446,0 0.0891,0 0.13364,0 0.0445,0 0.0891,0 0.13363,0 0.0223,0 0.0457,-0.007 0.0668,0 0.0473,0.01574 0.0853,0.05474 0.13364,0.06682 0.0432,0.0108 0.0891,0 0.13363,0 0.13364,0 0.26727,0 0.4009,0 0.07,0 0.34657,0.01357 0.40091,0 0.0483,-0.01209 0.0853,-0.05474 0.13364,-0.06682 0.0432,-0.0108 0.0891,0 0.13363,0 0.0445,0 0.0891,0 0.13363,0 0.043,0 0.42251,-0.0113 0.46773,0 0.0483,0.01206 0.0838,0.06682 0.13363,0.06682 0.0315,0 0.0369,-0.05686 0.0668,-0.06682 0.0141,-0.0047 0.30576,-0.0071 0.33408,0 0.0683,0.01709 0.13139,0.053 0.20046,0.06682 0.0852,0.01704 0.33318,-0.02257 0.4009,0 0.0299,0.0099 0.0369,0.05686 0.0668,0.06682 0.0423,0.01408 0.0891,0 0.13363,0 0.15591,0 0.31182,0 0.46773,0 0.0445,0 0.0904,-0.0108 0.13363,0 0.0483,0.01209 0.0853,0.05474 0.13363,0.06682 0.11602,0.029 0.2849,-0.029 0.40091,0 0.0483,0.01206 0.0853,0.05474 0.13363,0.06682 0.0864,0.02162 0.18084,-0.02162 0.26727,0 0.0483,0.01209 0.0864,0.05107 0.13364,0.06682 0.0211,0.007 0.0457,-0.007 0.0668,0 0.0472,0.01574 0.0853,0.05474 0.13364,0.06682 0.0432,0.0108 0.0904,-0.01079 0.13363,0 0.37857,0.189283 -0.0996,-0.0249 0.26728,0.06682 0.0966,0.02416 0.17063,0.109479 0.26726,0.133636 0.0432,0.01079 0.0914,-0.01408 0.13364,0 0.0299,0.0099 0.0369,0.05686 0.0668,0.06682 0.0423,0.01408 0.0914,-0.01408 0.13364,0 0.0299,0.0099 0.0353,0.06682 0.0668,0.06682 0.0498,0 0.0838,-0.06682 0.13363,-0.06682 0.0315,0 0.0353,0.06682 0.0668,0.06682 0.0315,0 0.0353,-0.06682 0.0668,-0.06682 0.0498,0 0.0864,0.05107 0.13363,0.06682 0.0211,0.007 0.0457,-0.007 0.0668,0 0.0472,0.01574 0.0864,0.05107 0.13363,0.06682 0.0211,0.007 0.0469,-0.0099 0.0668,0 0.0282,0.01407 0.0369,0.05686 0.0668,0.06681 0.0423,0.01408 0.0914,-0.01408 0.13363,0 0.0299,0.0099 0.0387,0.05273 0.0668,0.06682 0.0398,0.01992 0.0938,-0.01992 0.13364,0 0.0282,0.01407 0.0445,0.04454 0.0668,0.06682 0.0446,0 0.0914,-0.01408 0.13364,0 0.0299,0.0099 0.0386,0.05273 0.0668,0.06682 0.0398,0.01992 0.0938,-0.01992 0.13363,0 0.0282,0.01408 0.0387,0.05273 0.0668,0.06682 0.0424,0.02119 0.29068,-0.0217 0.33409,0 0.0282,0.01408 0.0386,0.05273 0.0668,0.06681 0.0398,0.01992 0.0914,-0.01407 0.13364,0 0.23033,0.07678 0.0495,0.06682 0.20045,0.06682 0.0223,0 0.0445,0 0.0668,0 0.0223,0 0.0469,-0.0099 0.0668,0 0.0282,0.01408 0.0369,0.05686 0.0668,0.06682 0.0634,0.02114 0.13364,0 0.20045,0 0.26727,0 0.53454,0 0.80181,0 0.0465,0 0.30993,-0.01209 0.33409,0 0.0282,0.01408 0.0386,0.05273 0.0668,0.06682 0.0422,0.02109 0.29193,-0.02109 0.33408,0 0.0282,0.01408 0.0387,0.05273 0.0668,0.06682 0.0398,0.01992 0.0938,-0.01992 0.13363,0 0.0282,0.01408 0.0386,0.05273 0.0668,0.06681 0.0399,0.01992 0.0938,-0.01992 0.13364,0 0.0282,0.01408 0.0386,0.05273 0.0668,0.06682 0.0199,0.0099 0.0469,-0.0099 0.0668,0 0.3058,0.1529 -0.28353,-0.02769 0.20045,0.133636 0.0423,0.01408 0.0938,-0.01992 0.13364,0 0.0282,0.01408 0.0386,0.05273 0.0668,0.06682 0.0398,0.01992 0.0938,-0.01992 0.13363,0 0.0282,0.01408 0.0353,0.06682 0.0668,0.06682 0.0223,0 -0.0157,-0.05107 0,-0.06682 0.0157,-0.01574 0.0511,-0.01574 0.0668,0 0.0157,0.01574 -0.0223,0.06682 0,0.06682 0.0315,0 0.0386,-0.05273 0.0668,-0.06682 0.0137,-0.0069 0.19103,-0.0094 0.20046,0 0.0157,0.01574 -0.0157,0.05107 0,0.06682 0.0157,0.01574 0.0511,-0.01574 0.0668,0 0.0158,0.01574 -0.0157,0.05107 0,0.06682 0.0315,0.0315 0.10214,-0.0315 0.13364,0 0.0157,0.01574 -0.0157,0.05107 0,0.06682 0.0315,0.0315 0.0938,-0.01992 0.13363,0 0.0282,0.01407 0.0386,0.05273 0.0668,0.06682 0.0265,0.01326 0.18679,-0.01365 0.20045,0 0.0157,0.01574 -0.0157,0.05107 0,0.06682 0.016,0.01601 0.26727,-0.01519 0.26727,0 0,0.02228 -0.0511,0.01574 -0.0668,0 -0.0157,-0.01574 0,-0.04454 0,-0.06682"

def path_to_points(path):
    spath = path.split(" ")
    origin = spath[1]
    deltas = spath[3:]
    print(deltas)

    points = []
    points.append(np.array([float(s) for s in origin.split(",")]))
    for delta in deltas:
        p0 = points[-1]
        dp = np.array(np.array([float(s) for s in delta.split(",")]))
        p1 = p0 + dp
        points.append(p1)

    return points

points = path_to_points(path)

x = []
y = []

for p in points:
    x.append(p[0]/145)
    y.append(1-p[1]/90)

plt.plot(x,savgol_filter(y, 2101, 2))
plt.plot(x,y)
plt.show()

print(x)
print(savgol_filter(y, 2101, 2))
