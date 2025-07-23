'''
Author: yiran-111 1179862677@qq.com
Date: 2025-07-23 11:30:03
LastEditors: yiran-111 1179862677@qq.com
LastEditTime: 2025-07-23 11:30:49
FilePath: \my_net\download_dataset.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import torchvision
torchvision.datasets.MNIST('./data', download=True)