"""
From https://docs.google.com/spreadsheets/d/12R3nCOLskxPYjjiNkdqy4OdQ65eQp_htebXGODsjSeA/edit#gid=0
Try to keep this list in sync with that.
"""
top_torch = [
    ("t", 6837449),
    ("tensor", 585786),
    ("mode", 462182),
    ("cat", 394818),
    ("max", 368038),
    ("zeros", 329495),
    ("load", 327756),
    ("no_grad", 294694),
    ("save", 265130),
    ("from_numpy", 243063),
    ("manual_seed", 165044),
    ("ones", 153696),
    ("randn", 150796),
    ("stack", 133358),
    ("sum", 130772),
    ("arange", 98087),
    ("rand", 94715),
    ("mean", 88546),
    ("exp", 73883),
    ("zeros_like", 72831),
    ("min", 72248),
    ("sigmoid", 66798),
    ("log", 62135),
    ("matmul", 47811),
    ("clamp", 45304),
    ("sqrt", 44911),
    ("abs", 43535),
    ("tanh", 42793),
    ("empty", 40311),
    ("argmax", 38435),
    ("bmm", 33984),
    ("pow", 33571),
    ("norm", 31125),
    ("mm", 30995),
    ("is_tensor", 29546),
    ("ones_like", 29512),
    ("nonzero", 28681),
    ("full", 28373),
    ("unsqueeze", 27911),
    ("where", 26585),
    ("randperm", 26450),
    ("eye", 24342),
    ("mul", 23236),
    ("topk", 22537),
    ("as_tensor", 21967),
    ("sort", 21412),
    ("squeeze", 20863),
    ("randint", 20771),
    ("linspace", 20041),
    ("add", 19201),
    ("transpose", 18663),
    ("split", 18325),
    ("gather", 17904),
    ("set_grad_enabled", 16013),
    ("sin", 15669),
    ("cos", 15562),
    ("div", 15513),
    ("index_select", 14866),
    ("multinomial", 14331),
    ("flatten", 14267),
    ("isnan", 14170),
    ("randn_like", 13096),
    ("eq", 12680),
    ("einsum", 12480),
    ("round", 12367),
    ("floor", 11628),
    ("allclose", 11000),
    ("reshape", 10605),
    ("diag", 10167),
    ("chunk", 9581),
    ("std", 9379),
    ("set_default_tensor_type", 9281),
    ("triu", 8559),
    ("meshgrid", 8292),
    ("set_num_threads", 8126),
    ("unique", 7964),
    ("full_like", 7780),
    ("tril", 7538),
    ("dot", 7275),
    ("sign", 6943),
    ("equal", 6916),
    ("normal", 6750),
    ("cumsum", 6556),
    ("dist", 6058),
    ("isfinite", 6030),
    ("gt", 5935),
    ("set_printoptions", 5888),
    ("range", 5491),
    ("empty_like", 5351),
    ("flip", 5342),
    ("masked_select", 5341),
    ("bernoulli", 5262),
    ("atan", 5253),
    ("var", 5247),
    ("prod", 5200),
    ("erf", 5088),
    ("inverse", 5072),
    ("addmm", 4854),
    ("logsumexp", 4582),
    ("fft", 4436),
    ("lt", 4421),
    ("log2", 4316),
    ("enable_grad", 4238),
    ("rand_like", 4187),
    ("argsort", 3972),
    ("seed", 3932),
    ("mv", 3547),
    ("ger", 3309),
    ("ge", 3248),
    ("atan2", 3210),
    ("ceil", 3202),
    ("ne", 3075),
    ("bincount", 3063),
    ("acos", 3055),
    ("rsqrt", 3031),
    ("svd", 3029),
    ("numel", 3003),
    ("log1p", 2840),
    ("unbind", 2808),
    ("le", 2714),
    ("isinf", 2707),
    ("cross", 2646),
    ("set_default_dtype", 2536),
    ("argmin", 2535),
    ("sparse_coo_tensor", 2489),
    ("log10", 2304),
    ("kthvalue", 2192),
    ("set_rng_state", 2158),
    ("get_rng_state", 1996),
    ("get_default_dtype", 1879),
    ("det", 1868),
    ("qr", 1864),
    ("histc", 1852),
    ("symeig", 1832),
    ("trace", 1801),
    ("median", 1795),
    ("addcmul", 1751),
    ("remainder", 1717),
    ("baddbmm", 1693),
    ("lgamma", 1665),
    ("repeat_interleave", 1598),
    ("fmod", 1576),
    ("reciprocal", 1575),
    ("tan", 1560),
    ("initial_seed", 1532),
    ("take", 1529),
    ("stft", 1487),
    ("get_num_threads", 1477),
    ("real", 1459),
    ("cholesky", 1406),
    ("quantize_per_tensor", 1392),
    ("diag_embed", 1364),
    ("lerp", 1363),
    ("asin", 1345),
    ("eig", 1333),
    ("trunc", 1290),
    ("diagonal", 1287),
    ("cosh", 1279),
    ("rfft", 1269),
    ("cumprod", 1260),
    ("addr", 1211),
    ("roll", 1198),
    ("narrow", 1188),
    ("digamma", 1172),
    ("square", 1163),
    ("sinh", 1131),
    ("logspace", 1084),
    ("broadcast_tensors", 1070),
    ("irfft", 1013),
    ("frac", 997),
    ("hann_window", 994),
    ("solve", 989),
    ("logdet", 977),
    ("expm1", 968),
    ("cdist", 946),
    ("addmv", 903),
    ("randint_like", 888),
    ("tensordot", 888),
    ("ifft", 877),
    ("true_divide", 854),
    ("erfinv", 830),
    ("addcdiv", 819),
    ("addbmm", 813),
    ("renorm", 781),
    ("pinverse", 753),
    ("isclose", 740),
    ("erfc", 729),
    ("is_storage", 725),
    ("triangular_solve", 723),
    ("rot90", 709),
    ("logical_not", 686),
    ("geqrf", 681),
    ("slogdet", 677),
    ("lu", 665),
    ("hamming_window", 659),
    ("orgqr", 651),
    ("ormqr", 622),
    ("is_floating_point", 602),
    ("diagflat", 562),
    ("cholesky_solve", 559),
    ("tril_indices", 552),
    ("chain_matmul", 551),
    ("triu_indices", 548),
    ("angle", 522),
    ("poisson", 505),
    ("matrix_power", 485),
    ("unique_consecutive", 471),
    ("quantize_per_channel", 465),
    ("std_mean", 458),
    ("bartlett_window", 447),
    ("var_mean", 428),
    ("lstsq", 421),
    ("logical_and", 419),
    ("mvlgamma", 411),
    ("blackman_window", 400),
    ("bitwise_not", 395),
    ("cholesky_inverse", 388),
    ("as_strided", 384),
    ("floor_divide", 353),
    ("cartesian_prod", 321),
    ("lu_solve", 317),
    ("set_flush_denormal", 310),
    ("empty_strided", 283),
    ("logical_xor", 282),
    ("polygamma", 282),
    ("logical_or", 280),
    ("set_num_interop_threads", 278),
    ("combinations", 274),
    ("trapz", 270),
    ("matrix_rank", 260),
    ("lu_unpack", 255),
    ("result_type", 244),
    ("conj", 231),
    ("cummax", 230),
    ("lobpcg", 229),
    ("bitwise_xor", 217),
    ("promote_types", 213),
    ("get_num_interop_threads", 211),
    ("cummin", 205),
    ("bitwise_and", 198),
    ("dequantize", 192),
    ("bitwise_or", 191),
    ("imag", 191),
    ("can_cast", 184),
    ("istft", 180),
    ("compiled_with_cxx11_abi", 159),
    ("is_complex", 151),
    ("block_diag", 136),
    ("pca_lowrank", 124),
    ("absolute", 122),
    ("svd_lowrank", 108),
    ("neg", 2),
]

top_nn_functional = [
    ("nn.functional.softmax", 10522),
    ("nn.functional.relu", 8572),
    ("nn.functional.interpolate", 7277),
    ("nn.functional.pad", 5207),
    ("nn.functional.log_softmax", 4699),
    ("nn.functional.normalize", 2338),
    ("nn.functional.cross_entropy", 2083),
    ("nn.functional.grid_sample", 1970),
    ("nn.functional.one_hot", 1967),
    ("nn.functional.mse_loss", 1920),
    ("nn.functional.conv2d", 1593),
    ("nn.functional.dropout", 1516),
    ("nn.functional.softplus", 1385),
    ("nn.functional.sigmoid", 1128),
    ("nn.functional.linear", 1036),
    ("nn.functional.gelu", 930),
    ("nn.functional.avg_pool2d", 899),
    ("nn.functional.max_pool2d", 876),
    ("nn.functional.nll_loss", 863),
    ("nn.functional.embedding", 737),
    ("nn.functional.tanh", 664),
    ("nn.functional.leaky_relu", 640),
    ("nn.functional.adaptive_avg_pool2d", 633),
    ("nn.functional.cosine_similarity", 627),
    ("nn.functional.unfold", 609),
    ("nn.functional.conv1d", 596),
    ("nn.functional.binary_cross_entropy_with_logits", 591),
    ("nn.functional.l1_loss", 571),
    ("nn.functional.binary_cross_entropy", 492),
    ("nn.functional.elu", 416),
    ("nn.functional.batch_norm", 413),
    ("nn.functional.upsample", 413),
    ("nn.functional.fold", 305),
    ("nn.functional.affine_grid", 298),
    ("nn.functional.max_pool1d", 297),
    ("nn.functional.torch", 294),
    ("nn.functional.threshold", 263),
    ("nn.functional.smooth_l1_loss", 262),
    ("nn.functional.pairwise_distance", 253),
    ("nn.functional.logsigmoid", 243),
    ("nn.functional.adaptive_max_pool2d", 235),
    ("nn.functional.relu6", 213),
    ("nn.functional.pixel_shuffle", 209),
    ("nn.functional.avg_pool3d", 203),
    ("nn.functional.bilinear", 203),
    ("nn.functional.conv_transpose2d", 201),
    ("nn.functional.gumbel_softmax", 197),
    ("nn.functional.max_unpool2d", 196),
    ("nn.functional.kl_div", 191),
    ("nn.functional.hardtanh", 189),
    ("nn.functional.ctc_loss", 185),
    ("nn.functional.layer_norm", 178),
    ("nn.functional.conv3d", 172),
    ("nn.functional.max_unpool3d", 167),
    ("nn.functional.hardshrink", 165),
    ("nn.functional.hardswish", 156),
    ("nn.functional.selu", 156),
    ("nn.functional.glu", 155),
    ("nn.functional.assert_int_or_pair", 150),
    ("nn.functional.hardsigmoid", 146),
    ("nn.functional.upsample_bilinear", 146),
    ("nn.functional.max_pool3d", 140),
    ("nn.functional.adaptive_avg_pool3d", 139),
    ("nn.functional.instance_norm", 124),
    ("nn.functional.embedding_bag", 122),
    ("nn.functional.upsample_nearest", 110),
    ("nn.functional.avg_pool1d", 105),
    ("nn.functional.prelu", 102),
    ("nn.functional.celu", 92),
    ("nn.functional.dropout2d", 86),
    ("nn.functional.hinge_embedding_loss", 82),
    ("nn.functional.softsign", 81),
    ("nn.functional.max_unpool1d", 74),
    ("nn.functional.silu", 74),
    ("nn.functional.softshrink", 70),
    ("nn.functional.leaky_relu_", 68),
    ("nn.functional.softmin", 67),
    ("nn.functional.channel_shuffle", 66),
    ("nn.functional.multilabel_margin_loss", 66),
    ("nn.functional.dropout3d", 65),
    ("nn.functional.multi_margin_loss", 65),
    ("nn.functional.lp_pool2d", 64),
    ("nn.functional.conv_transpose1d", 62),
    ("nn.functional.triplet_margin_loss", 62),
    ("nn.functional.tanhshrink", 61),
    ("nn.functional.adaptive_max_pool1d", 59),
    ("nn.functional.cosine_embedding_loss", 58),
    ("nn.functional.multi_head_attention_forward", 58),
    ("nn.functional.max_pool1d_with_indices", 53),
    ("nn.functional.poisson_nll_loss", 53),
    ("nn.functional.margin_ranking_loss", 52),
    ("nn.functional.soft_margin_loss", 52),
    ("nn.functional.adaptive_max_pool3d", 51),
    ("nn.functional.group_norm", 51),
    ("nn.functional.local_response_norm", 51),
    ("nn.functional.multilabel_soft_margin_loss", 51),
    ("nn.functional.relu_", 50),
    ("nn.functional.alpha_dropout", 49),
    ("nn.functional.feature_alpha_dropout", 49),
    ("nn.functional.lp_pool1d", 49),
    ("nn.functional.adaptive_max_pool1d_with_indices", 48),
    ("nn.functional.adaptive_max_pool2d_with_indices", 48),
    ("nn.functional.adaptive_max_pool3d_with_indices", 48),
    ("nn.functional.fractional_max_pool2d", 48),
    ("nn.functional.fractional_max_pool2d_with_indices", 48),
    ("nn.functional.fractional_max_pool3d", 48),
    ("nn.functional.fractional_max_pool3d_with_indices", 48),
    ("nn.functional.max_pool2d_with_indices", 48),
    ("nn.functional.max_pool3d_with_indices", 48),
    ("nn.functional.handle_torch_function", 47),
    ("nn.functional.has_torch_function", 47),
    ("nn.functional.adaptive_avg_pool1d", 43),
    ("nn.functional.pdist", 43),
    ("nn.functional.rrelu_", 37),
    ("nn.functional.elu_", 34),
    ("nn.functional.boolean_dispatch", 33),
    ("nn.functional.hardtanh_", 26),
    ("nn.functional.triplet_margin_with_distance_loss", 23),
    ("nn.functional.selu_", 20),
    ("nn.functional.pixel_unshuffle", 19),
    ("nn.functional.conv_transpose3d", 18),
    ("nn.functional.gaussian_nll_loss", 15),
    ("nn.functional.has_torch_function_unary", 15),
    ("nn.functional.has_torch_function_variadic", 15),
    ("nn.functional.celu_", 13),
    ("nn.functional.huber_loss", 7),
    ("nn.functional.mish", 4),
    ("nn.functional.threshold_", 3),
    ("nn.functional.grad", 2),
    ("nn.functional.conv_tbc", 1),
    ("nn.functional.math", 1),
]

top_nn_module = [
    ("nn.Module", 927129, None),
    ("nn.Linear", 530688, "nn.functional.linear"),
    ("nn.Sequential", 384968, None),
    ("nn.Conv2d", 383320, "nn.functional.conv2d"),
    ("nn.ReLU", 318877, "nn.functional.relu"),
    ("nn.BatchNorm2d", 233265, "nn.functional.batch_norm"),
    ("nn.Dropout", 179268, "nn.functional.dropout"),
    ("nn.ModuleList", 171225, None),
    ("nn.Parameter", 153291, None),
    ("nn.CrossEntropyLoss", 152696, "nn.functional.cross_entropy"),
    ("nn.MaxPool2d", 138619, "nn.functional.max_pool2d"),
    ("nn.Embedding", 111844, "nn.functional.embedding"),
    ("nn.DataParallel", 104238, None),
    ("nn.MSELoss", 82954, "nn.functional.mse_loss"),
    ("nn.Sigmoid", 75810, "nn.functional.sigmoid"),
    ("nn.LeakyReLU", 65632, "nn.functional.leaky_relu"),
    ("nn.BatchNorm1d", 65374, "nn.functional.batch_norm"),
    ("nn.Softmax", 65114, "nn.functional.softmax"),
    ("nn.Tanh", 59445, "nn.functional.tanh"),
    ("nn.AdaptiveAvgPool2d", 59071, "nn.functional.adaptive_avg_pool2d"),
    ("nn.AvgPool2d", 58377, "nn.functional.avg_pool2d"),
    ("nn.ConvTranspose2d", 57524, "nn.functional.conv_transpose2d"),
    ("nn.LSTM", 57411, None),
    ("nn.Conv1d", 41108, "nn.functional.conv1d"),
    ("nn.LayerNorm", 36089, "nn.functional.layer_norm"),
    ("nn.BCELoss", 34005, "nn.functional.binary_cross_entropy"),
    ("nn.Upsample", 32527, "nn.functional.interpolate"),
    ("nn.BCEWithLogitsLoss", 29944, "nn.functional.binary_cross_entropy_with_logits"),
    ("nn.GRU", 25421, None),
    ("nn.Dropout2d", 23512, "nn.functional.dropout2d"),
    ("nn.LogSoftmax", 22897, "nn.functional.log_softmax"),
    ("nn.L1Loss", 22778, "nn.functional.l1_loss"),
    ("nn.GroupNorm", 22183, "nn.functional.group_norm"),
    ("nn.NLLLoss", 21751, "nn.functional.nll_loss"),
    ("nn.Conv3d", 20874, "nn.functional.conv3d"),
    ("nn.Identity", 17911, None),
    ("nn.InstanceNorm2d", 16426, "nn.functional.instance_norm"),
    ("nn.BatchNorm3d", 16378, "nn.functional.batch_norm"),
    ("nn.PReLU", 13472, "nn.functional.prelu"),
    ("nn.ReLU6", 12622, "nn.functional.relu6"),
    ("nn.ELU", 12508, "nn.functional.elu"),
    ("nn.LSTMCell", 10885, None),
    ("nn.Flatten", 10384, "torch.flatten"),
    ("nn.ModuleDict", 10255, None),
    ("nn.ReflectionPad2d", 9954, "nn.functional.pad"),
    ("nn.MaxPool3d", 9526, "nn.functional.max_pool3d"),
    ("nn.MaxPool1d", 9154, "nn.functional.max_pool1d"),
    ("nn.RNN", 9154, None),
    ("nn.ZeroPad2d", 8847, "nn.functional.pad"),
    ("nn.ParameterList", 7702, None),
    ("nn.SyncBatchNorm", 6814, None),
    ("nn.PixelShuffle", 6571, "nn.functional.pixel_shuffle"),
    ("nn.SmoothL1Loss", 6517, "nn.functional.smooth_l1_loss"),
    ("nn.Hardswish", 6458, "nn.functional.hardswish"),
    ("nn.AdaptiveMaxPool2d", 6071, "nn.functional.adaptive_max_pool2d"),
    ("nn.SELU", 6043, "nn.functional.selu"),
    ("nn.ConvTranspose3d", 6039, "nn.functional.conv_transpose3d"),
    ("nn.GRUCell", 5840, None),
    ("nn.ReplicationPad2d", 5600, "nn.functional.pad"),
    ("nn.KLDivLoss", 5541, "nn.functional.kl_div"),
    ("nn.ConvTranspose1d", 5183, "nn.functional.conv_transpose1d"),
    ("nn.Softplus", 5120, "nn.functional.softplus"),
    ("nn.SiLU", 4895, "nn.functional.silu"),
    ("nn.AvgPool3d", 4523, "nn.functional.avg_pool3d"),
    ("nn.CosineSimilarity", 4058, "nn.functional.cosine_similarity"),
    ("nn.GELU", 3932, "nn.functional.gelu"),
    ("nn.UpsamplingBilinear2d", 3673, "nn.functional.interpolate"),
    ("nn.InstanceNorm1d", 3658, "nn.functional.instance_norm"),
    ("nn.Transformer", 3604, None),
    ("nn.MultiheadAttention", 3435, "nn.functional.multi_head_attention_forward"),
    ("nn.AvgPool1d", 3195, "nn.functional.avg_pool1d"),
    ("nn.Dropout3d", 2964, "nn.functional.dropout3d"),
    ("nn.AdaptiveAvgPool3d", 2915, "nn.functional.adaptive_avg_pool3d"),
    ("nn.InstanceNorm3d", 2893, "nn.functional.instance_norm"),
    ("nn.Hardtanh", 2613, "nn.functional.hardtanh"),
    ("nn.MarginRankingLoss", 2568, "nn.functional.margin_ranking_loss"),
    ("nn.GLU", 2526, "nn.functional.glu"),
    ("nn.AdaptiveAvgPool1d", 2481, "nn.functional.adaptive_avg_pool1d"),
    ("nn.EmbeddingBag", 2344, "nn.functional.embedding_bag"),
    ("nn.TransformerEncoderLayer", 2292, None),
    ("nn.TransformerEncoder", 2091, None),
    ("nn.MaxUnpool2d", 2031, "nn.functional.max_unpool2d"),
    ("nn.UpsamplingNearest2d", 2004, "nn.functional.interpolate"),
    ("nn.ConstantPad1d", 1904, "nn.functional.pad"),
    ("nn.ConstantPad2d", 1791, "nn.functional.pad"),
    ("nn.CTCLoss", 1789, "nn.functional.ctc_loss"),
    ("nn.AdaptiveMaxPool1d", 1713, "nn.functional.adaptive_max_pool1d"),
    ("nn.AdaptiveLogSoftmaxWithLoss", 1665, None),
    ("nn.Bilinear", 1664, "nn.functional.bilinear"),
    ("nn.RNNCell", 1653, None),
    ("nn.MultiLabelSoftMarginLoss", 1624, "nn.functional.multilabel_soft_margin_loss"),
    ("nn.Unfold", 1452, "nn.functional.unfold"),
    ("nn.RReLU", 1431, "nn.functional.rrelu"),
    ("nn.CosineEmbeddingLoss", 1357, "nn.functional.cosine_embedding_loss"),
    ("nn.LocalResponseNorm", 1331, "nn.functional.local_response_norm"),
    ("nn.Softmax2d", 1300, "nn.functional.softmax"),
    ("nn.PairwiseDistance", 1241, "nn.functional.pairwise_distance"),
    ("nn.LogSigmoid", 1235, "nn.functional.logsigmoid"),
    ("nn.TripletMarginLoss", 1230, "nn.functional.triplet_margin_loss"),
    ("nn.RNNBase", 1133, None),
    ("nn.Threshold", 1043, "nn.functional.threshold"),
    ("nn.AdaptiveMaxPool3d", 1025, "nn.functional.adaptive_max_pool3d"),
    ("nn.CELU", 1018, "nn.functional.celu"),
    ("nn.NLLLoss2d", 966, "nn.functional.nll_loss"),
    ("nn.Softsign", 877, "nn.functional.softsign"),
    ("nn.ReplicationPad1d", 862, "nn.functional.pad"),
    ("nn.SoftMarginLoss", 856, "nn.functional.soft_margin_loss"),
    ("nn.ParameterDict", 742, None),
    ("nn.ReflectionPad1d", 731, "nn.functional.pad"),
    ("nn.Softshrink", 713, "nn.functional.softshrink"),
    ("nn.AlphaDropout", 710, "nn.functional.alpha_dropout"),
    ("nn.Tanhshrink", 681, "nn.functional.tanhshrink"),
    ("nn.PoissonNLLLoss", 676, "nn.functional.poisson_nll_loss"),
    ("nn.MaxUnpool3d", 660, "nn.functional.max_unpool3d"),
    ("nn.Fold", 630, "nn.functional.fold"),
    ("nn.MultiMarginLoss", 622, "nn.functional.multi_margin_loss"),
    ("nn.TransformerDecoderLayer", 614, None),
    ("nn.TransformerDecoder", 607, None),
    ("nn.Hardshrink", 592, "nn.functional.hardshrink"),
    ("nn.ConstantPad3d", 582, "nn.functional.pad"),
    ("nn.MultiLabelMarginLoss", 580, "nn.functional.multilabel_margin_loss"),
    ("nn.LPPool2d", 550, "nn.functional.lp_pool2d"),
    ("nn.Softmin", 537, "nn.functional.softmin"),
    ("nn.MaxUnpool1d", 518, "nn.functional.max_unpool1d"),
    ("nn.FractionalMaxPool2d", 484, "nn.functional.fractional_max_pool2d"),
    ("nn.Hardsigmoid", 477, "nn.functional.hardsigmoid"),
    ("nn.ReplicationPad3d", 470, "nn.functional.pad"),
    ("nn.HingeEmbeddingLoss", 442, "nn.functional.hinge_embedding_loss"),
    ("nn.LPPool1d", 386, "nn.functional.lp_pool1d"),
    ("nn.FractionalMaxPool3d", 252, "nn.functional.fractional_max_pool3d"),
    ("nn.Container", 217, None),
    ("nn.Unflatten", 206, "nn.functional.unflatten"),
    ("nn.FeatureAlphaDropout", 136, "nn.functional.feature_alpha_dropout"),
    ("nn.TripletMarginWithDistanceLoss", 107, "nn.functional.triplet_margin_with_distance_loss"),
    ("nn.ChannelShuffle", 90, "nn.functional.channel_shuffle"),
    ("nn.RNNCellBase", 88, None),
    ("nn.LazyLinear", 81, "nn.functional.linear"),
    ("nn.UninitializedParameter", 60, None),
    ("nn.CrossMapLRN2d", 59, None),
    ("nn.GaussianNLLLoss", 55, "nn.functional.gaussian_nll_loss"),
    ("nn.PixelUnshuffle", 45, "nn.functional.pixel_unshuffle"),
    ("nn.Mish", 31, "nn.functional.mish"),
    ("nn.ReflectionPad3d", 22, "nn.functional.pad"),
    ("nn.HuberLoss", 18, "nn.functional.huber_loss"),
    ("nn.LazyConv2d", 15, None),
    ("nn.LazyConv1d", 9, None),
    ("nn.LazyConv3d", 8, None),
    ("nn.LazyConvTranspose1d", 8, None),
    ("nn.LazyConvTranspose2d", 8, None),
    ("nn.LazyConvTranspose3d", 8, None),
    ("nn.LazyBatchNorm1d", 3, None),
    ("nn.LazyBatchNorm2d", 3, None),
    ("nn.LazyBatchNorm3d", 3, None),
    ("nn.UninitializedBuffer", 3, None),
]

# No rankings because these are a little hard to get rankings for
method_only_ops = [
    'bfloat16',
    'bool',
    'byte',
    'char',
    'contiguous',
    'cpu',
    'cuda',
    'detach',
    'double',
    'expand',
    'expand_as',
    'float',
    'get_device',
    'half',
    'hardshrink',
    'index_add',
    'index_copy',
    'index_fill',
    'index_put',
    'int',
    'is_contiguous',
    'is_pinned',
    'is_set_to',
    'is_shared',
    'is_signed',
    'item',
    'long',
    'masked_scatter',
    'masked_fill',
    'narrow_copy',
    'numpy',
    'pin_memory',
    'repeat',
    'reshape_as',
    'select',
    'short',
    'storage_offset',
    'sum_to_size',
    'to',
    'to_mkldnn',
    'tolist',
    'type',
    'type_as',
    'unfold',
    'view',
    'view_as',
]

def get_nn_functional_top_list():
    top_nn_functional_ = {k: v for k, v in top_nn_functional}
    for _, count, functional_name in top_nn_module:
        if functional_name is None:
            continue
        if functional_name == 'torch.flatten':
            continue
        if functional_name not in top_nn_functional_:
            top_nn_functional_[functional_name] = count
        else:
            top_nn_functional_[functional_name] += count

    top_nn_functional_ = [(k, v) for k, v in top_nn_functional_.items()]
    top_nn_functional_.sort(key=lambda x: x[1], reverse=True)
    return top_nn_functional_

usage_count = {}
for k, v in get_nn_functional_top_list():
    usage_count[k] = v
for k, v in top_torch:
    usage_count[k] = v
