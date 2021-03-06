def code():
    """
    Example G-code module, a heart.

    Source: https://commons.wikimedia.org/wiki/File:A_perfect_SVG_heart.svg#/media/File:Bezier_SVG_heart_horizontal.svg

    Please simulate first, before milling.
    """

    return """
        G90
        G1 X-0.2685 Y-0.0008
        G1 X-0.5428 Y-0.0048
        G1 X-0.7280 Y-0.0091
        G1 X-0.9134 Y-0.0150
        G1 X-1.1859 Y-0.0262
        G1 X-1.3749 Y-0.0358
        G1 X-1.6515 Y-0.0528
        G1 X-1.8395 Y-0.0658
        G1 X-2.0279 Y-0.0805
        G1 X-2.2146 Y-0.0965
        G1 X-2.4945 Y-0.1229
        G1 X-2.7778 Y-0.1529
        G1 X-2.9705 Y-0.1750
        G1 X-3.2535 Y-0.2103
        G1 X-3.4476 Y-0.2365
        G1 X-3.7323 Y-0.2774
        G1 X-3.9274 Y-0.3071
        G1 X-4.2136 Y-0.3536
        G1 X-4.4100 Y-0.3871
        G1 X-4.6980 Y-0.4389
        G1 X-4.8951 Y-0.4762
        G1 X-5.0907 Y-0.5148
        G1 X-5.2870 Y-0.5550
        G1 X-5.5781 Y-0.6172
        G1 X-5.7770 Y-0.6614
        G1 X-5.9746 Y-0.7069
        G1 X-6.1730 Y-0.7541
        G1 X-6.4669 Y-0.8263
        G1 X-6.6695 Y-0.8783
        G1 X-6.8687 Y-0.9306
        G1 X-7.0671 Y-0.9842
        G1 X-7.2672 Y-1.0396
        G1 X-7.4694 Y-1.0973
        G1 X-7.6690 Y-1.1554
        G1 X-7.8722 Y-1.2164
        G1 X-8.0721 Y-1.2774
        G1 X-8.2761 Y-1.3416
        G1 X-8.4768 Y-1.4059
        G1 X-8.6815 Y-1.4729
        G1 X-8.8847 Y-1.5413
        G1 X-9.0886 Y-1.6111
        G1 X-9.2923 Y-1.6822
        G1 X-9.5979 Y-1.7920
        G1 X-9.7041 Y-1.8306
        G1 X-9.9088 Y-1.9068
        G1 X-10.1143 Y-1.9845
        G1 X-10.4224 Y-2.1041
        G1 X-10.6314 Y-2.1869
        G1 X-10.8379 Y-2.2705
        G1 X-11.0449 Y-2.3553
        G1 X-11.2540 Y-2.4427
        G1 X-11.5649 Y-2.5755
        G1 X-11.7762 Y-2.6678
        G1 X-12.0881 Y-2.8067
        G1 X-12.3000 Y-2.9030
        G1 X-12.5108 Y-3.0005
        G1 X-12.7206 Y-3.0988
        G1 X-13.0355 Y-3.2492
        G1 X-13.2489 Y-3.3530
        G1 X-13.5651 Y-3.5098
        G1 X-13.7793 Y-3.6180
        G1 X-13.9929 Y-3.7274
        G1 X-14.2042 Y-3.8372
        G1 X-14.4191 Y-3.9502
        G1 X-14.6327 Y-4.0645
        G1 X-14.8455 Y-4.1796
        G1 X-15.0602 Y-4.2972
        G1 X-15.2761 Y-4.4173
        G1 X-15.4905 Y-4.5380
        G1 X-15.7066 Y-4.6611
        G1 X-15.9215 Y-4.7853
        G1 X-16.1374 Y-4.9113
        G1 X-16.4610 Y-5.1039
        G1 X-16.6782 Y-5.2347
        G1 X-16.8969 Y-5.3685
        G1 X-17.1133 Y-5.5021
        G1 X-17.3307 Y-5.6380
        G1 X-17.6568 Y-5.8448
        G1 X-17.9840 Y-6.0561
        G1 X-18.2052 Y-6.2009
        G1 X-18.4234 Y-6.3452
        G1 X-18.6441 Y-6.4930
        G1 X-18.9713 Y-6.7152
        G1 X-19.1935 Y-6.8681
        G1 X-19.4135 Y-7.0211
        G1 X-19.6340 Y-7.1760
        G1 X-19.8554 Y-7.3335
        G1 X-20.0762 Y-7.4917
        G1 X-20.2984 Y-7.6533
        G1 X-20.6289 Y-7.8958
        G1 X-20.8532 Y-8.0627
        G1 X-21.0754 Y-8.2298
        G1 X-21.2971 Y-8.3980
        G1 X-21.6309 Y-8.6545
        G1 X-21.9659 Y-8.9162
        G1 X-22.1910 Y-9.0940
        G1 X-22.4145 Y-9.2720
        G1 X-22.6385 Y-9.4523
        G1 X-22.8626 Y-9.6342
        G1 X-23.0878 Y-9.8189
        G1 X-23.3129 Y-10.0053
        G1 X-23.5377 Y-10.1930
        G1 X-23.7625 Y-10.3825
        G1 X-24.0998 Y-10.6703
        G1 X-24.2146 Y-10.7688
        G1 X-24.4407 Y-10.9649
        G1 X-24.6662 Y-11.1620
        G1 X-24.8923 Y-11.3614
        G1 X-25.1188 Y-11.5631
        G1 X-25.3451 Y-11.7660
        G1 X-25.5730 Y-11.9723
        G1 X-25.7996 Y-12.1795
        G1 X-26.1399 Y-12.4937
        G1 X-26.3683 Y-12.7068
        G1 X-26.5964 Y-12.9212
        G1 X-26.8244 Y-13.1376
        G1 X-27.0530 Y-13.3568
        G1 X-27.2811 Y-13.5765
        G1 X-27.5095 Y-13.7988
        G1 X-27.7383 Y-14.0233
        G1 X-27.9672 Y-14.2494
        G1 X-28.1968 Y-14.4788
        G1 X-28.4254 Y-14.7084
        G1 X-28.6555 Y-14.9413
        G1 X-28.9987 Y-15.2926
        G1 X-29.2298 Y-15.5316
        G1 X-29.5740 Y-15.8907
        G1 X-29.8051 Y-16.1343
        G1 X-30.1498 Y-16.5011
        G1 X-30.4960 Y-16.8740
        G1 X-30.6134 Y-17.0015
        G1 X-30.8435 Y-17.2527
        G1 X-31.0744 Y-17.5064
        G1 X-31.4206 Y-17.8912
        G1 X-31.6522 Y-18.1503
        G1 X-31.8849 Y-18.4135
        G1 X-32.1158 Y-18.6761
        G1 X-32.2324 Y-18.8092
        G1 X-32.5791 Y-19.2090
        G1 X-32.8122 Y-19.4800
        G1 X-33.0444 Y-19.7523
        G1 X-33.2763 Y-20.0259
        G1 X-33.5090 Y-20.3022
        G1 X-33.7419 Y-20.5816
        G1 X-33.9743 Y-20.8618
        G1 X-34.2070 Y-21.1445
        G1 X-34.4399 Y-21.4295
        G1 X-34.6728 Y-21.7167
        G1 X-34.9060 Y-22.0060
        G1 X-35.2552 Y-22.4434
        G1 X-35.6050 Y-22.8864
        G1 X-35.8394 Y-23.1856
        G1 X-36.1887 Y-23.6352
        G1 X-36.4236 Y-23.9405
        G1 X-36.6570 Y-24.2461
        G1 X-36.8907 Y-24.5539
        G1 X-37.1247 Y-24.8638
        G1 X-37.4752 Y-25.3329
        G1 X-37.7099 Y-25.6499
        G1 X-37.9438 Y-25.9674
        G1 X-38.1782 Y-26.2882
        G1 X-38.4119 Y-26.6098
        G1 X-38.7635 Y-27.0980
        G1 X-39.1147 Y-27.5905
        G1 X-39.3499 Y-27.9235
        G1 X-39.5844 Y-28.2570
        G1 X-39.8193 Y-28.5938
        G1 X-40.0533 Y-28.9311
        G1 X-40.2885 Y-29.2727
        G1 X-40.5232 Y-29.6159
        G1 X-40.8745 Y-30.1335
        G1 X-41.2268 Y-30.6580
        G1 X-41.4617 Y-31.0106
        G1 X-41.6969 Y-31.3659
        G1 X-41.9313 Y-31.7223
        G1 X-42.1666 Y-32.0822
        G1 X-42.4012 Y-32.4429
        G1 X-42.7530 Y-32.9895
        G1 X-42.9885 Y-33.3573
        G1 X-43.2234 Y-33.7276
        G1 X-43.5752 Y-34.2857
        G1 X-43.9275 Y-34.8503
        G1 X-44.2798 Y-35.4203
        G1 X-44.6324 Y-35.9959
        G1 X-44.7505 Y-36.1899
        G1 X-45.1018 Y-36.7711
        G1 X-45.2204 Y-36.9682
        G1 X-45.2707 Y-37.0583
        G1 X-45.3095 Y-37.1394
        G1 X-45.3438 Y-37.2222
        G1 X-45.3733 Y-37.3070
        G1 X-45.3979 Y-37.3934
        G1 X-45.4178 Y-37.4810
        G1 X-45.4325 Y-37.5696
        G1 X-45.4421 Y-37.6588
        G1 X-45.4467 Y-37.7485
        G1 X-45.4465 Y-37.8384
        G1 X-45.4409 Y-37.9280
        G1 X-45.4302 Y-38.0172
        G1 X-45.4147 Y-38.1056
        G1 X-45.3941 Y-38.1930
        G1 X-45.3687 Y-38.2791
        G1 X-45.3385 Y-38.3636
        G1 X-45.3035 Y-38.4462
        G1 X-45.2638 Y-38.5270
        G1 X-45.2196 Y-38.6049
        G1 X-44.9870 Y-38.9913
        G1 X-44.7528 Y-39.3784
        G1 X-44.5173 Y-39.7645
        G1 X-44.2829 Y-40.1467
        G1 X-43.9313 Y-40.7157
        G1 X-43.5788 Y-41.2806
        G1 X-43.2265 Y-41.8399
        G1 X-42.9908 Y-42.2107
        G1 X-42.7563 Y-42.5778
        G1 X-42.4045 Y-43.1236
        G1 X-42.0523 Y-43.6654
        G1 X-41.6997 Y-44.2018
        G1 X-41.4647 Y-44.5569
        G1 X-41.2295 Y-44.9097
        G1 X-40.8788 Y-45.4322
        G1 X-40.5265 Y-45.9514
        G1 X-40.2913 Y-46.2953
        G1 X-40.0566 Y-46.6362
        G1 X-39.7050 Y-47.1421
        G1 X-39.4701 Y-47.4779
        G1 X-39.2356 Y-47.8109
        G1 X-38.8849 Y-48.3044
        G1 X-38.6492 Y-48.6331
        G1 X-38.4155 Y-48.9572
        G1 X-38.0647 Y-49.4393
        G1 X-37.8298 Y-49.7599
        G1 X-37.5961 Y-50.0763
        G1 X-37.2456 Y-50.5468
        G1 X-37.1277 Y-50.7040
        G1 X-36.8938 Y-51.0144
        G1 X-36.6601 Y-51.3220
        G1 X-36.4267 Y-51.6275
        G1 X-36.1932 Y-51.9311
        G1 X-35.9593 Y-52.2328
        G1 X-35.7259 Y-52.5318
        G1 X-35.4922 Y-52.8292
        G1 X-35.2595 Y-53.1233
        G1 X-34.9105 Y-53.5605
        G1 X-34.6763 Y-53.8510
        G1 X-34.3279 Y-54.2798
        G1 X-34.0942 Y-54.5648
        G1 X-33.8615 Y-54.8465
        G1 X-33.5138 Y-55.2638
        G1 X-33.2801 Y-55.5419
        G1 X-33.0477 Y-55.8160
        G1 X-32.8160 Y-56.0875
        G1 X-32.5839 Y-56.3578
        G1 X-32.2367 Y-56.7578
        G1 X-32.0038 Y-57.0238
        G1 X-31.6583 Y-57.4149
        G1 X-31.4246 Y-57.6765
        G1 X-31.1943 Y-57.9328
        G1 X-31.0782 Y-58.0616
        G1 X-30.8473 Y-58.3153
        G1 X-30.6167 Y-58.5671
        G1 X-30.5001 Y-58.6935
        G1 X-30.1562 Y-59.0641
        G1 X-29.9245 Y-59.3113
        G1 X-29.6944 Y-59.5546
        G1 X-29.3502 Y-59.9155
        G1 X-29.1196 Y-60.1551
        G1 X-29.0030 Y-60.2750
        G1 X-28.6609 Y-60.6252
        G1 X-28.4305 Y-60.8589
        G1 X-28.0876 Y-61.2028
        G1 X-27.9710 Y-61.3186
        G1 X-27.7429 Y-61.5444
        G1 X-27.5141 Y-61.7687
        G1 X-27.2857 Y-61.9910
        G1 X-27.0574 Y-62.2114
        G1 X-26.8298 Y-62.4291
        G1 X-26.6012 Y-62.6463
        G1 X-26.3733 Y-62.8607
        G1 X-26.1455 Y-63.0730
        G1 X-25.9187 Y-63.2831
        G1 X-25.8039 Y-63.3887
        G1 X-25.5773 Y-63.5955
        G1 X-25.3505 Y-63.8010
        G1 X-25.1242 Y-64.0042
        G1 X-24.8976 Y-64.2059
        G1 X-24.6710 Y-64.4058
        G1 X-24.4455 Y-64.6031
        G1 X-24.2192 Y-64.7989
        G1 X-24.1059 Y-64.8967
        G1 X-23.8808 Y-65.0890
        G1 X-23.5443 Y-65.3735
        G1 X-23.3182 Y-65.5625
        G1 X-23.0937 Y-65.7484
        G1 X-22.8679 Y-65.9333
        G1 X-22.6449 Y-66.1149
        G1 X-22.4201 Y-66.2955
        G1 X-22.1966 Y-66.4738
        G1 X-21.9733 Y-66.6501
        G1 X-21.6398 Y-66.9104
        G1 X-21.3055 Y-67.1677
        G1 X-21.0805 Y-67.3384
        G1 X-20.8593 Y-67.5048
        G1 X-20.6373 Y-67.6702
        G1 X-20.4145 Y-67.8340
        G1 X-20.0848 Y-68.0740
        G1 X-19.7528 Y-68.3118
        G1 X-19.5298 Y-68.4692
        G1 X-19.2016 Y-68.6984
        G1 X-18.9799 Y-68.8510
        G1 X-18.7597 Y-69.0009
        G1 X-18.5402 Y-69.1487
        G1 X-18.2136 Y-69.3656
        G1 X-17.8849 Y-69.5802
        G1 X-17.6657 Y-69.7215
        G1 X-17.4473 Y-69.8604
        G1 X-17.1222 Y-70.0644
        G1 X-16.9032 Y-70.1997
        G1 X-16.6870 Y-70.3318
        G1 X-16.4686 Y-70.4637
        G1 X-16.2537 Y-70.5917
        G1 X-15.9309 Y-70.7812
        G1 X-15.7135 Y-70.9069
        G1 X-15.4988 Y-71.0296
        G1 X-15.1778 Y-71.2097
        G1 X-14.8562 Y-71.3867
        G1 X-14.6393 Y-71.5040
        G1 X-14.4270 Y-71.6176
        G1 X-14.2139 Y-71.7301
        G1 X-13.8956 Y-71.8947
        G1 X-13.6822 Y-72.0034
        G1 X-13.4684 Y-72.1106
        G1 X-13.1537 Y-72.2655
        G1 X-13.0452 Y-72.3184
        G1 X-12.8344 Y-72.4195
        G1 X-12.6238 Y-72.5188
        G1 X-12.4138 Y-72.6166
        G1 X-12.3076 Y-72.6656
        G1 X-12.0988 Y-72.7606
        G1 X-11.7871 Y-72.8995
        G1 X-11.5761 Y-72.9917
        G1 X-11.3657 Y-73.0816
        G1 X-11.1592 Y-73.1690
        G1 X-10.9515 Y-73.2551
        G1 X-10.7432 Y-73.3402
        G1 X-10.5369 Y-73.4228
        G1 X-10.2299 Y-73.5431
        G1 X-9.9205 Y-73.6610
        G1 X-9.6119 Y-73.7751
        G1 X-9.4041 Y-73.8500
        G1 X-9.2001 Y-73.9221
        G1 X-9.0968 Y-73.9582
        G1 X-8.8946 Y-74.0275
        G1 X-8.6909 Y-74.0959
        G1 X-8.3881 Y-74.1947
        G1 X-8.1847 Y-74.2594
        G1 X-7.9809 Y-74.3227
        G1 X-7.7813 Y-74.3831
        G1 X-7.5786 Y-74.4431
        G1 X-7.3779 Y-74.5010
        G1 X-7.1788 Y-74.5571
        G1 X-6.9776 Y-74.6122
        G1 X-6.7800 Y-74.6651
        G1 X-6.5784 Y-74.7171
        G1 X-6.3820 Y-74.7669
        G1 X-6.1839 Y-74.8154
        G1 X-5.9860 Y-74.8624
        G1 X-5.7879 Y-74.9081
        G1 X-5.5911 Y-74.9521
        G1 X-5.3002 Y-75.0143
        G1 X-5.1024 Y-75.0550
        G1 X-4.9065 Y-75.0936
        G1 X-4.7115 Y-75.1306
        G1 X-4.4237 Y-75.1827
        G1 X-4.2278 Y-75.2162
        G1 X-3.9413 Y-75.2627
        G1 X-3.7465 Y-75.2927
        G1 X-3.4620 Y-75.3336
        G1 X-3.1750 Y-75.3717
        G1 X-2.8905 Y-75.4062
        G1 X-2.6972 Y-75.4281
        G1 X-2.5098 Y-75.4476
        G1 X-2.2299 Y-75.4743
        G1 X-1.9492 Y-75.4979
        G1 X-1.7585 Y-75.5122
        G1 X-1.4818 Y-75.5299
        G1 X-1.2949 Y-75.5404
        G1 X-1.1087 Y-75.5492
        G1 X-0.9251 Y-75.5566
        G1 X-0.7417 Y-75.5627
        G1 X-0.5570 Y-75.5670
        G1 X-0.2873 Y-75.5711
        G1 X-0.0145 Y-75.5721
        G1 X0.1707 Y-75.5708
        G1 X0.3485 Y-75.5683
        G1 X0.5303 Y-75.5642
        G1 X0.7092 Y-75.5589
        G1 X0.8877 Y-75.5520
        G1 X0.9779 Y-75.5482
        G1 X1.1554 Y-75.5393
        G1 X1.4163 Y-75.5238
        G1 X1.6815 Y-75.5048
        G1 X1.8603 Y-75.4901
        G1 X1.9489 Y-75.4822
        G1 X2.1209 Y-75.4659
        G1 X2.2946 Y-75.4481
        G1 X2.4681 Y-75.4291
        G1 X2.6408 Y-75.4085
        G1 X2.8130 Y-75.3867
        G1 X2.9847 Y-75.3633
        G1 X3.1534 Y-75.3392
        G1 X3.3233 Y-75.3133
        G1 X3.4127 Y-75.2991
        G1 X3.6591 Y-75.2579
        G1 X3.9111 Y-75.2127
        G1 X4.1605 Y-75.1647
        G1 X4.3307 Y-75.1299
        G1 X4.4940 Y-75.0956
        G1 X4.6596 Y-75.0590
        G1 X4.8247 Y-75.0209
        G1 X4.9863 Y-74.9823
        G1 X5.1496 Y-74.9419
        G1 X5.3104 Y-74.9008
        G1 X5.4722 Y-74.8579
        G1 X5.7089 Y-74.7923
        G1 X5.8712 Y-74.7458
        G1 X6.0310 Y-74.6981
        G1 X6.2626 Y-74.6267
        G1 X6.4239 Y-74.5749
        G1 X6.5791 Y-74.5238
        G1 X6.7358 Y-74.4702
        G1 X6.8887 Y-74.4169
        G1 X7.0416 Y-74.3620
        G1 X7.1948 Y-74.3059
        G1 X7.2725 Y-74.2767
        G1 X7.4236 Y-74.2188
        G1 X7.6462 Y-74.1307
        G1 X7.8003 Y-74.0677
        G1 X7.9466 Y-74.0067
        G1 X8.0967 Y-73.9424
        G1 X8.2438 Y-73.8779
        G1 X8.4615 Y-73.7796
        G1 X8.6078 Y-73.7118
        G1 X8.7533 Y-73.6427
        G1 X8.8981 Y-73.5724
        G1 X9.1092 Y-73.4669
        G1 X9.2519 Y-73.3941
        G1 X9.3952 Y-73.3191
        G1 X9.4668 Y-73.2808
        G1 X9.6710 Y-73.1698
        G1 X9.8118 Y-73.0915
        G1 X9.9504 Y-73.0128
        G1 X10.0863 Y-72.9338
        G1 X10.2222 Y-72.8535
        G1 X10.3573 Y-72.7720
        G1 X10.4917 Y-72.6892
        G1 X10.6881 Y-72.5652
        G1 X10.8222 Y-72.4789
        G1 X10.9545 Y-72.3915
        G1 X11.0838 Y-72.3049
        G1 X11.2756 Y-72.1733
        G1 X11.4061 Y-72.0814
        G1 X11.5316 Y-71.9917
        G1 X11.7198 Y-71.8538
        G1 X11.9052 Y-71.7143
        G1 X12.0906 Y-71.5711
        G1 X12.2156 Y-71.4723
        G1 X12.3358 Y-71.3755
        G1 X12.4577 Y-71.2757
        G1 X12.6319 Y-71.1299
        G1 X12.7523 Y-71.0270
        G1 X12.8709 Y-70.9234
        G1 X12.9855 Y-70.8218
        G1 X13.1005 Y-70.7179
        G1 X13.2151 Y-70.6128
        G1 X13.3271 Y-70.5084
        G1 X13.4394 Y-70.4017
        G1 X13.6045 Y-70.2411
        G1 X13.7142 Y-70.1327
        G1 X13.8247 Y-70.0212
        G1 X13.9327 Y-69.9102
        G1 X14.0383 Y-69.7997
        G1 X14.1953 Y-69.6323
        G1 X14.3012 Y-69.5167
        G1 X14.4048 Y-69.4019
        G1 X14.5555 Y-69.2310
        G1 X14.6576 Y-69.1129
        G1 X14.7579 Y-68.9948
        G1 X14.8570 Y-68.8759
        G1 X15.0010 Y-68.6994
        G1 X15.0988 Y-68.5772
        G1 X15.1943 Y-68.4555
        G1 X15.2888 Y-68.3328
        G1 X15.3812 Y-68.2107
        G1 X15.4737 Y-68.0867
        G1 X15.6078 Y-67.9026
        G1 X15.6990 Y-67.7746
        G1 X15.8295 Y-67.5868
        G1 X15.9174 Y-67.4581
        G1 X16.0449 Y-67.2663
        G1 X16.0891 Y-67.1990
        G1 X16.2120 Y-67.0072
        G1 X16.2956 Y-66.8741
        G1 X16.3759 Y-66.7436
        G1 X16.4566 Y-66.6097
        G1 X16.5730 Y-66.4126
        G1 X16.6507 Y-66.2780
        G1 X16.7279 Y-66.1408
        G1 X16.8029 Y-66.0060
        G1 X16.8770 Y-65.8688
        G1 X16.9837 Y-65.6679
        G1 X17.0904 Y-65.4604
        G1 X17.1277 Y-65.3862
        G1 X17.2288 Y-65.1810
        G1 X17.2966 Y-65.0402
        G1 X17.3952 Y-64.8294
        G1 X17.4602 Y-64.6869
        G1 X17.5240 Y-64.5439
        G1 X17.6162 Y-64.3308
        G1 X17.7061 Y-64.1164
        G1 X17.7381 Y-64.0387
        G1 X17.8234 Y-63.8249
        G1 X17.8808 Y-63.6770
        G1 X17.9629 Y-63.4594
        G1 X18.0431 Y-63.2384
        G1 X18.0965 Y-63.0867
        G1 X18.1473 Y-62.9384
        G1 X18.1971 Y-62.7883
        G1 X18.2684 Y-62.5668
        G1 X18.3167 Y-62.4121
        G1 X18.3619 Y-62.2630
        G1 X18.4066 Y-62.1101
        G1 X18.4704 Y-61.8848
        G1 X18.5328 Y-61.6537
        G1 X18.5537 Y-61.5739
        G1 X18.5928 Y-61.4205
        G1 X18.6306 Y-61.2666
        G1 X18.6850 Y-61.0367
        G1 X18.7211 Y-60.8772
        G1 X18.7546 Y-60.7222
        G1 X18.7876 Y-60.5655
        G1 X18.8194 Y-60.4073
        G1 X18.8496 Y-60.2503
        G1 X18.8785 Y-60.0939
        G1 X18.9197 Y-59.8571
        G1 X18.9583 Y-59.6201
        G1 X18.9834 Y-59.4555
        G1 X19.0063 Y-59.2968
        G1 X19.0281 Y-59.1350
        G1 X19.0487 Y-58.9752
        G1 X19.0683 Y-58.8147
        G1 X19.0866 Y-58.6519
        G1 X19.1112 Y-58.4121
        G1 X19.1267 Y-58.2463
        G1 X19.1470 Y-58.0050
        G1 X19.1645 Y-57.7596
        G1 X19.1750 Y-57.5925
        G1 X19.1877 Y-57.3489
        G1 X19.1978 Y-57.1000
        G1 X19.2032 Y-56.9336
        G1 X19.2085 Y-56.6882
        G1 X19.2113 Y-56.4378
        G1 X19.2115 Y-56.3501
        G1 X19.2110 Y-56.1848
        G1 X19.2077 Y-55.9366
        G1 X19.2021 Y-55.6880
        G1 X19.1932 Y-55.4335
        G1 X19.1859 Y-55.2645
        G1 X19.1724 Y-55.0136
        G1 X19.1559 Y-54.7596
        G1 X19.1432 Y-54.5889
        G1 X19.1292 Y-54.4187
        G1 X19.1140 Y-54.2485
        G1 X19.0889 Y-53.9963
        G1 X19.0609 Y-53.7421
        G1 X19.0299 Y-53.4860
        G1 X19.0073 Y-53.3126
        G1 X18.9837 Y-53.1409
        G1 X18.9585 Y-52.9694
        G1 X18.9192 Y-52.7154
        G1 X18.8905 Y-52.5412
        G1 X18.8460 Y-52.2867
        G1 X18.8140 Y-52.1122
        G1 X18.7813 Y-51.9399
        G1 X18.7470 Y-51.7672
        G1 X18.6939 Y-51.5120
        G1 X18.6367 Y-51.2516
        G1 X18.5773 Y-50.9943
        G1 X18.5351 Y-50.8183
        G1 X18.4704 Y-50.5597
        G1 X18.4257 Y-50.3867
        G1 X18.3789 Y-50.2115
        G1 X18.3312 Y-50.0380
        G1 X18.2580 Y-49.7814
        G1 X18.2059 Y-49.6042
        G1 X18.1541 Y-49.4322
        G1 X18.0736 Y-49.1736
        G1 X18.0172 Y-48.9981
        G1 X17.9314 Y-48.7393
        G1 X17.8717 Y-48.5638
        G1 X17.7805 Y-48.3042
        G1 X17.6870 Y-48.0454
        G1 X17.6210 Y-47.8678
        G1 X17.5224 Y-47.6103
        G1 X17.4528 Y-47.4332
        G1 X17.3830 Y-47.2592
        G1 X17.3126 Y-47.0865
        G1 X17.2397 Y-46.9118
        G1 X17.1668 Y-46.7398
        G1 X17.0911 Y-46.5645
        G1 X16.9763 Y-46.3060
        G1 X16.8976 Y-46.1317
        G1 X16.8176 Y-45.9582
        G1 X16.7353 Y-45.7835
        G1 X16.6527 Y-45.6108
        G1 X16.5273 Y-45.3535
        G1 X16.4389 Y-45.1769
        G1 X16.3086 Y-44.9209
        G1 X16.2169 Y-44.7446
        G1 X16.0805 Y-44.4878
        G1 X16.0332 Y-44.4000
        G1 X15.8920 Y-44.1427
        G1 X15.7472 Y-43.8846
        G1 X15.6466 Y-43.7091
        G1 X15.4983 Y-43.4546
        G1 X15.4447 Y-43.3639
        G1 X15.3431 Y-43.1940
        G1 X15.2382 Y-43.0217
        G1 X15.1328 Y-42.8506
        G1 X15.0264 Y-42.6806
        G1 X14.8631 Y-42.4243
        G1 X14.7518 Y-42.2529
        G1 X14.6388 Y-42.0809
        G1 X14.5250 Y-41.9102
        G1 X14.4099 Y-41.7406
        G1 X14.2933 Y-41.5701
        G1 X14.1755 Y-41.4007
        G1 X14.1150 Y-41.3146
        G1 X13.9951 Y-41.1455
        G1 X13.8130 Y-40.8935
        G1 X13.6883 Y-40.7233
        G1 X13.5621 Y-40.5536
        G1 X13.4356 Y-40.3857
        G1 X13.3076 Y-40.2176
        G1 X13.1130 Y-39.9669
        G1 X12.9149 Y-39.7159
        G1 X12.7782 Y-39.5458
        G1 X12.6426 Y-39.3791
        G1 X12.4368 Y-39.1307
        G1 X12.2969 Y-38.9636
        G1 X12.1547 Y-38.7965
        G1 X11.9431 Y-38.5508
        G1 X11.7950 Y-38.3822
        G1 X11.6494 Y-38.2181
        G1 X11.5014 Y-38.0533
        G1 X11.3520 Y-37.8889
        G1 X11.2573 Y-37.7860
        G1 X11.3454 Y-37.6903
        G1 X11.4950 Y-37.5260
        G1 X11.6428 Y-37.3614
        G1 X11.8603 Y-37.1160
        G1 X12.0068 Y-36.9473
        G1 X12.1488 Y-36.7825
        G1 X12.2895 Y-36.6171
        G1 X12.4302 Y-36.4495
        G1 X12.6342 Y-36.2029
        G1 X12.7724 Y-36.0334
        G1 X12.9065 Y-35.8668
        G1 X13.0403 Y-35.6977
        G1 X13.2347 Y-35.4490
        G1 X13.3652 Y-35.2791
        G1 X13.4935 Y-35.1099
        G1 X13.6804 Y-34.8592
        G1 X13.8064 Y-34.6878
        G1 X13.9875 Y-34.4371
        G1 X14.1681 Y-34.1820
        G1 X14.2877 Y-34.0098
        G1 X14.4043 Y-33.8402
        G1 X14.5194 Y-33.6697
        G1 X14.6332 Y-33.4998
        G1 X14.7455 Y-33.3291
        G1 X14.8570 Y-33.1569
        G1 X14.9657 Y-32.9872
        G1 X15.0208 Y-32.9006
        G1 X15.1280 Y-32.7289
        G1 X15.2331 Y-32.5590
        G1 X15.3373 Y-32.3875
        G1 X15.4406 Y-32.2153
        G1 X15.5428 Y-32.0418
        G1 X15.6901 Y-31.7876
        G1 X15.8364 Y-31.5290
        G1 X15.8869 Y-31.4388
        G1 X15.9809 Y-31.2679
        G1 X16.0749 Y-31.0947
        G1 X16.1663 Y-30.9230
        G1 X16.2573 Y-30.7500
        G1 X16.3464 Y-30.5770
        G1 X16.4346 Y-30.4040
        G1 X16.5207 Y-30.2316
        G1 X16.6063 Y-30.0573
        G1 X16.7300 Y-29.8000
        G1 X16.8122 Y-29.6250
        G1 X16.9314 Y-29.3659
        G1 X17.0475 Y-29.1064
        G1 X17.1242 Y-28.9314
        G1 X17.1628 Y-28.8419
        G1 X17.2715 Y-28.5844
        G1 X17.3439 Y-28.4096
        G1 X17.4480 Y-28.1513
        G1 X17.5168 Y-27.9761
        G1 X17.6164 Y-27.7160
        G1 X17.6814 Y-27.5415
        G1 X17.7454 Y-27.3657
        G1 X17.8366 Y-27.1089
        G1 X17.8679 Y-27.0195
        G1 X17.9273 Y-26.8450
        G1 X17.9850 Y-26.6720
        G1 X18.0414 Y-26.4993
        G1 X18.1231 Y-26.2400
        G1 X18.1770 Y-26.0645
        G1 X18.2532 Y-25.8074
        G1 X18.3037 Y-25.6309
        G1 X18.3751 Y-25.3746
        G1 X18.4224 Y-25.1983
        G1 X18.4886 Y-24.9400
        G1 X18.5318 Y-24.7675
        G1 X18.5740 Y-24.5920
        G1 X18.6144 Y-24.4185
        G1 X18.6530 Y-24.2468
        G1 X18.6903 Y-24.0761
        G1 X18.7442 Y-23.8183
        G1 X18.7790 Y-23.6441
        G1 X18.8275 Y-23.3891
        G1 X18.8735 Y-23.1300
        G1 X18.9027 Y-22.9578
        G1 X18.9436 Y-22.7017
        G1 X18.9814 Y-22.4462
        G1 X19.0058 Y-22.2720
        G1 X19.0281 Y-22.1003
        G1 X19.0589 Y-21.8478
        G1 X19.0784 Y-21.6743
        G1 X19.1043 Y-21.4226
        G1 X19.1280 Y-21.1691
        G1 X19.1422 Y-20.9959
        G1 X19.1549 Y-20.8257
        G1 X19.1663 Y-20.6591
        G1 X19.1808 Y-20.4069
        G1 X19.1892 Y-20.2369
        G1 X19.1988 Y-19.9875
        G1 X19.2019 Y-19.8996
        G1 X19.2075 Y-19.6510
        G1 X19.2108 Y-19.4028
        G1 X19.2115 Y-19.2326
        G1 X19.2108 Y-19.0650
        G1 X19.2090 Y-18.9006
        G1 X19.2057 Y-18.7338
        G1 X19.2011 Y-18.5671
        G1 X19.1922 Y-18.3246
        G1 X19.1884 Y-18.2374
        G1 X19.1757 Y-17.9949
        G1 X19.1656 Y-17.8277
        G1 X19.1483 Y-17.5854
        G1 X19.1282 Y-17.3411
        G1 X19.1127 Y-17.1755
        G1 X19.0881 Y-16.9349
        G1 X19.0698 Y-16.7708
        G1 X19.0502 Y-16.6083
        G1 X19.0297 Y-16.4483
        G1 X19.0081 Y-16.2890
        G1 X18.9850 Y-16.1275
        G1 X18.9611 Y-15.9690
        G1 X18.9225 Y-15.7317
        G1 X18.8816 Y-15.4955
        G1 X18.8516 Y-15.3327
        G1 X18.8216 Y-15.1765
        G1 X18.7904 Y-15.0200
        G1 X18.7574 Y-14.8620
        G1 X18.7068 Y-14.6314
        G1 X18.6527 Y-14.3980
        G1 X18.6337 Y-14.3170
        G1 X18.5956 Y-14.1633
        G1 X18.5567 Y-14.0099
        G1 X18.4765 Y-13.7091
        G1 X18.4109 Y-13.4770
        G1 X18.3657 Y-13.3225
        G1 X18.2976 Y-13.0983
        G1 X18.2263 Y-12.8732
        G1 X18.1524 Y-12.6494
        G1 X18.1005 Y-12.4970
        G1 X18.0487 Y-12.3492
        G1 X17.9695 Y-12.1305
        G1 X17.8869 Y-11.9108
        G1 X17.8288 Y-11.7610
        G1 X17.7437 Y-11.5473
        G1 X17.6535 Y-11.3294
        G1 X17.5621 Y-11.1155
        G1 X17.4975 Y-10.9687
        G1 X17.4338 Y-10.8270
        G1 X17.3378 Y-10.6190
        G1 X17.2692 Y-10.4744
        G1 X17.2009 Y-10.3340
        G1 X17.1336 Y-10.1973
        G1 X17.0617 Y-10.0558
        G1 X16.9921 Y-9.9205
        G1 X16.8846 Y-9.7168
        G1 X16.8089 Y-9.5773
        G1 X16.7343 Y-9.4422
        G1 X16.6583 Y-9.3078
        G1 X16.5809 Y-9.1727
        G1 X16.4648 Y-8.9756
        G1 X16.3838 Y-8.8415
        G1 X16.2631 Y-8.6459
        G1 X16.1785 Y-8.5123
        G1 X16.0967 Y-8.3850
        G1 X16.0104 Y-8.2532
        G1 X15.9263 Y-8.1272
        G1 X15.8382 Y-7.9977
        G1 X15.7089 Y-7.8118
        G1 X15.6184 Y-7.6840
        G1 X15.4836 Y-7.4986
        G1 X15.3886 Y-7.3708
        G1 X15.2964 Y-7.2494
        G1 X15.2029 Y-7.1277
        G1 X15.1074 Y-7.0058
        G1 X14.9654 Y-6.8285
        G1 X14.8648 Y-6.7056
        G1 X14.7670 Y-6.5882
        G1 X14.6670 Y-6.4701
        G1 X14.5656 Y-6.3528
        G1 X14.4650 Y-6.2380
        G1 X14.3131 Y-6.0683
        G1 X14.2062 Y-5.9517
        G1 X14.0510 Y-5.7856
        G1 X13.9410 Y-5.6708
        G1 X13.8346 Y-5.5611
        G1 X13.7256 Y-5.4508
        G1 X13.5618 Y-5.2893
        G1 X13.4511 Y-5.1816
        G1 X13.3373 Y-5.0734
        G1 X13.1707 Y-4.9182
        G1 X13.0528 Y-4.8108
        G1 X12.8824 Y-4.6589
        G1 X12.7645 Y-4.5557
        G1 X12.6449 Y-4.4531
        G1 X12.4694 Y-4.3061
        G1 X12.4079 Y-4.2553
        G1 X12.2278 Y-4.1097
        G1 X12.1046 Y-4.0119
        G1 X11.9222 Y-3.8707
        G1 X11.7963 Y-3.7752
        G1 X11.6086 Y-3.6365
        G1 X11.5443 Y-3.5895
        G1 X11.3553 Y-3.4549
        G1 X11.1635 Y-3.3215
        G1 X10.9680 Y-3.1895
        G1 X10.8351 Y-3.1018
        G1 X10.6390 Y-2.9756
        G1 X10.5026 Y-2.8897
        G1 X10.3693 Y-2.8075
        G1 X10.2342 Y-2.7257
        G1 X10.0983 Y-2.6451
        G1 X9.9616 Y-2.5659
        G1 X9.8247 Y-2.4877
        G1 X9.6855 Y-2.4102
        G1 X9.5471 Y-2.3345
        G1 X9.4061 Y-2.2591
        G1 X9.2664 Y-2.1854
        G1 X9.0559 Y-2.0780
        G1 X8.9093 Y-2.0051
        G1 X8.7665 Y-1.9357
        G1 X8.6213 Y-1.8666
        G1 X8.4066 Y-1.7671
        G1 X8.2560 Y-1.6995
        G1 X8.1089 Y-1.6350
        G1 X7.9611 Y-1.5715
        G1 X7.8841 Y-1.5390
        G1 X7.6647 Y-1.4488
        G1 X7.5854 Y-1.4168
        G1 X7.4348 Y-1.3576
        G1 X7.2847 Y-1.3000
        G1 X7.1305 Y-1.2426
        G1 X6.9802 Y-1.1874
        G1 X6.8234 Y-1.1321
        G1 X6.6690 Y-1.0787
        G1 X6.5156 Y-1.0272
        G1 X6.2824 Y-0.9517
        G1 X6.1211 Y-0.9014
        G1 X5.9639 Y-0.8539
        G1 X5.8824 Y-0.8296
        G1 X5.7249 Y-0.7841
        G1 X5.5659 Y-0.7396
        G1 X5.4038 Y-0.6960
        G1 X5.1653 Y-0.6340
        G1 X5.0805 Y-0.6126
        G1 X4.9169 Y-0.5730
        G1 X4.7546 Y-0.5349
        G1 X4.6713 Y-0.5159
        G1 X4.5080 Y-0.4795
        G1 X4.3416 Y-0.4442
        G1 X4.1778 Y-0.4110
        G1 X4.0101 Y-0.3782
        G1 X3.7622 Y-0.3322
        G1 X3.5103 Y-0.2888
        G1 X3.3373 Y-0.2608
        G1 X3.1661 Y-0.2349
        G1 X2.9959 Y-0.2103
        G1 X2.8262 Y-0.1872
        G1 X2.6540 Y-0.1651
        G1 X2.4811 Y-0.1445
        G1 X2.3078 Y-0.1252
        G1 X2.1336 Y-0.1074
        G1 X1.9593 Y-0.0909
        G1 X1.7841 Y-0.0757
        G1 X1.6952 Y-0.0686
        G1 X1.5214 Y-0.0554
        G1 X1.4298 Y-0.0493
        G1 X1.2553 Y-0.0383
        G1 X1.0780 Y-0.0287
        G1 X0.9878 Y-0.0244
        G1 X0.8095 Y-0.0168
        G1 X0.6332 Y-0.0107
        G1 X0.3655 Y-0.0041
        G1 X0.1826 Y-0.0013
        G1 X-0.0000 Y0.0000
    """
