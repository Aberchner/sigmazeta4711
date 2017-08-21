# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 20:24:54 2017

@author: Alex
"""

import math
import matplotlib.pyplot as plt
import numpy as np

values = [-33.7, -27.2, -20.9, -19.0, -18.4, -18.3, -17.3, -17.0, -16.2, -15.6, -15.5, -15.4, -15.2, -14.7, -14.6, -14.5, -14.4, -14.3, -14.1, -14.0, -13.6, -12.9, -12.8, -12.6, -12.4, -12.3, -12.1, -12.0, -11.9, -11.7, -11.6, -11.5, -11.4, -11.3, -11.2, -11.1, -11.0, -10.9, -10.8, -10.7, -10.6, -10.5, -10.3, -10.2, -10.1, -10.0, -9.9, -9.8, -9.6, -9.5, -9.4, -9.3, -9.2, -9.1, -8.9, -8.8, -8.6, -8.5, -8.3, -8.2, -8.1, -8.0, -7.9, -7.8, -7.7, -7.6, -7.5, -7.4, -7.3, -7.2, -7.1, -7.0, -6.9, -6.8, -6.7, -6.6, -6.5, -6.4, -6.3, -6.2, -6.1, -6.0, -5.9, -5.8, -5.7, -5.6, -5.5, -5.4, -5.3, -5.2, -5.1, -5.0, -4.9, -4.8, -4.7, -4.6, -4.5, -4.4, -4.3, -4.2, -4.1, -4.0, -3.9, -3.8, -3.7, -3.6, -3.5, -3.4, -3.3, -3.2, -3.1, -3.0, -2.9, -2.8, -2.7, -2.6, -2.5, -2.4, -2.3, -2.2, -2.1, -2.0, -1.9, -1.8, -1.7, -1.6, -1.5, -1.4, -1.3, -1.2, -1.1, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 7.0, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 8.0, 8.1, 8.2, 8.4, 8.6, 8.8, 9.0, 9.1, 9.3, 9.4, 9.5, 9.7, 9.8, 9.9, 10.1, 10.3, 10.5, 10.9, 11.1, 11.3, 11.8, 11.9, 12.5, 13.2, 13.5, 15.4, 15.9, 16.5, 16.9, 17.2, 17.3, 18.3, 20.2, 21.2, 24.8, 29.2]
density = [3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 6.499237639424896e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 6.499237639424896e-07, 3.249618819712448e-07, 3.249618819712448e-07, 6.499237639424896e-07, 6.499237639424896e-07, 6.499237639424896e-07, 3.249618819712448e-07, 3.249618819712448e-07, 6.499237639424896e-07, 3.249618819712448e-07, 6.499237639424896e-07, 3.249618819712448e-07, 6.499237639424896e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 9.748856459137344e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 6.499237639424896e-07, 3.249618819712448e-07, 6.499237639424896e-07, 6.499237639424896e-07, 6.499237639424896e-07, 6.499237639424896e-07, 1.2998475278849791e-06, 3.249618819712448e-07, 3.249618819712448e-07, 1.2998475278849791e-06, 3.249618819712448e-07, 2.5996950557699583e-06, 1.624809409856224e-06, 1.624809409856224e-06, 1.2998475278849791e-06, 1.9497712918274687e-06, 6.499237639424896e-07, 1.624809409856224e-06, 1.624809409856224e-06, 1.2998475278849791e-06, 1.624809409856224e-06, 2.2747331737987135e-06, 1.624809409856224e-06, 2.2747331737987135e-06, 2.924656937741203e-06, 1.624809409856224e-06, 4.549466347597427e-06, 3.899542583654937e-06, 2.2747331737987135e-06, 2.2747331737987135e-06, 3.899542583654937e-06, 2.5996950557699583e-06, 5.849313875482406e-06, 2.5996950557699583e-06, 1.9497712918274687e-06, 4.549466347597427e-06, 3.249618819712448e-06, 3.5745807016836926e-06, 4.224504465626182e-06, 4.224504465626182e-06, 3.899542583654937e-06, 4.224504465626182e-06, 6.8241995213961405e-06, 6.8241995213961405e-06, 9.098932695194854e-06, 8.12404704928112e-06, 9.098932695194854e-06, 1.1698627750964812e-05, 1.1373665868993567e-05, 1.4623284688706015e-05, 1.2348551514907302e-05, 2.0797560446159666e-05, 1.8197865390389708e-05, 2.1447484210102156e-05, 2.2747331737987135e-05, 2.7296798085584562e-05, 2.5347026793757093e-05, 2.17724460920734e-05, 3.444595948895195e-05, 3.8995425836549374e-05, 4.289496842020431e-05, 5.036909170554294e-05, 5.751825310891032e-05, 5.6868329344967834e-05, 7.18165759156451e-05, 7.636604226324253e-05, 9.098932695194854e-05, 0.00010593757352262579, 0.00010268795470291335, 0.00012543528644090048, 0.00015695658899211122, 0.0001813287301399546, 0.0002141498802190503, 0.00025152049664574344, 0.0003194375299777336, 0.000387679525191695, 0.00045527159664171394, 0.0005625090176922247, 0.000703542474467745, 0.0009105431932834279, 0.0010811481813183313, 0.0014766267916773363, 0.0019312484645551077, 0.0024726349599192014, 0.0033952017428355652, 0.004652479264182312, 0.006528159246920336, 0.009310482880358134, 0.013637025376923287, 0.020628580267534617, 0.03210818371005081, 0.051798599024334445, 0.0859065981560363, 0.14065000175479417, 0.23739537852209935, 0.14055608777090448, 0.08595696724774184, 0.05192240950136549, 0.03231355961945664, 0.02083005663435679, 0.0138414264006832, 0.009335179983387948, 0.0065837277287374195, 0.00469114972813689, 0.0034192489221014375, 0.002491482749073534, 0.0019176000655123154, 0.001435031670785017, 0.001140291243837098, 0.0008569244827581724, 0.0006872943803691827, 0.0005657586365119371, 0.00045527159664171394, 0.0003831300588440976, 0.00031326325422027996, 0.00024827087782603103, 0.00020895049010751039, 0.000185878196487552, 0.00015143223699860006, 0.0001377838379558078, 0.00011601139186373438, 0.00010593757352262579, 9.683864082743094e-05, 8.70897843682936e-05, 6.336756698439274e-05, 5.751825310891032e-05, 5.036909170554294e-05, 4.744443476780174e-05, 3.9970311482463105e-05, 3.347107384303821e-05, 3.184626443318199e-05, 2.6321912439670827e-05, 2.047259856418842e-05, 1.754794162644722e-05, 2.17724460920734e-05, 2.2097407974044645e-05, 2.112252232813091e-05, 1.2023589632936057e-05, 1.1698627750964812e-05, 1.2998475278849791e-05, 1.0398780223079833e-05, 1.1373665868993567e-05, 1.0073818341108588e-05, 8.77397081322361e-06, 8.12404704928112e-06, 7.149161403367385e-06, 4.874428229568672e-06, 4.224504465626182e-06, 4.224504465626182e-06, 6.174275757453651e-06, 2.5996950557699583e-06, 4.874428229568672e-06, 5.524351993511161e-06, 3.5745807016836926e-06, 5.849313875482406e-06, 3.249618819712448e-06, 1.9497712918274687e-06, 5.524351993511161e-06, 1.2998475278849791e-06, 2.924656937741203e-06, 3.899542583654937e-06, 1.2998475278849791e-06, 9.748856459137344e-07, 1.9497712918274687e-06, 1.9497712918274687e-06, 1.9497712918274687e-06, 1.9497712918274687e-06, 9.748856459137344e-07, 9.748856459137344e-07, 9.748856459137344e-07, 1.624809409856224e-06, 6.499237639424896e-07, 6.499237639424896e-07, 3.249618819712448e-07, 6.499237639424896e-07, 9.748856459137344e-07, 6.499237639424896e-07, 3.249618819712448e-07, 9.748856459137344e-07, 3.249618819712448e-07, 9.748856459137344e-07, 3.249618819712448e-07, 3.249618819712448e-07, 6.499237639424896e-07, 6.499237639424896e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 6.499237639424896e-07, 9.748856459137344e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07, 3.249618819712448e-07]