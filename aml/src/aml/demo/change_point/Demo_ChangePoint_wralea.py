
# This file has been generated at $TIME

from openalea.core import *

def register_packages(pkgmanager):
    
    metainfo = {'description': 'Change point detection.', 'license': '', 'url': '', 'version': '0.1', 'authors': 'Y. Guedon', 'institutes': 'CIRAD'} 
    pkg = UserPackage("Demo.ChangePoint", metainfo)

    

    nf = CompositeNodeFactory(name='Corsican pine change point', 
                              description='', 
                              category='Stat',
                              doc='',
                              inputs=[],
                              outputs=[],
                              elt_factory=\
{2: ('vplants.stat', 'Load_from_file'),
 3: ('vplants.stat', 'PlotSegmentProfile (gnuplot)'),
 4: ('vplants.stat', 'Cluster'),
 5: ('vplants.stat', 'SelectVariable'),
 6: ('vplants.stat', 'PlotSegmentProfile (gnuplot)'),
 7: ('vplants.stat', 'Segmentation'),
 8: ('vplants.stat', 'SelectVariable'),
 9: ('vplants.stat', 'SelectVariable'),
 10: ('vplants.stat', 'PlotData (gnuplot)'),
 11: ('vplants.stat', 'Segmentation'),
 12: ('vplants.stat', 'PlotData (gnuplot)'),
 13: ('vplants.stat', 'SegmentationSample'),
 14: ('vplants.stat', 'SelectIndividual'),
 15: ('vplants.stat', 'PlotData (gnuplot)'),
 16: ('Catalog.Data', 'int'),
 17: ('Catalog.Data', 'int'),
 18: ('vplants.stat', 'SegmentationSample'),
 19: ('vplants.stat', 'ComputeCorrelation multivariate'),
 20: ('vplants.stat', 'Plot (gnuplot)'),
 21: ('vplants.stat', 'SelectVariable'),
 22: ('vplants.stat', 'PointwiseAverage'),
 23: ('vplants.stat', 'PlotData (gnuplot)'),
 24: ('vplants.stat', 'SelectIndividual'),
 25: ('vplants.stat', 'PlotData (gnuplot)'),
 26: ('vplants.stat', 'Vectors'),
 27: ('vplants.stat', 'Regression'),
 28: ('vplants.stat', 'Plot (gnuplot)'),
 29: ('System', 'annotation'),
 30: ('System', 'annotation'),
 31: ('System', 'annotation'),
 32: ('System', 'annotation'),
 33: ('System', 'annotation'),
 34: ('Catalog.Data', 'packagedir'),
 35: ('Catalog.Data', 'filename'),
 36: ('System', 'annotation'),
 37: ('System', 'annotation'),
 38: ('System', 'annotation'),
 41: ('System', 'annotation'),
 42: ('System', 'annotation'),
 43: ('System', 'annotation'),
 44: ('System', 'annotation'),
 45: ('System', 'annotation')},
                              elt_connections=\
{140840528: (16, 0, 14, 1),
 140840540: (26, 0, 27, 0),
 140840552: (8, 0, 12, 0),
 140840564: (5, 0, 13, 0),
 140840576: (2, 0, 25, 0),
 140840588: (4, 0, 6, 0),
 140840600: (5, 0, 7, 0),
 140840612: (5, 0, 3, 0),
 140840624: (5, 0, 11, 0),
 140840636: (4, 0, 5, 0),
 140840648: (17, 0, 14, 1),
 140840660: (5, 0, 18, 0),
 140840672: (21, 0, 26, 0),
 140840684: (35, 0, 2, 0),
 140840696: (18, 0, 19, 0),
 140840708: (24, 0, 23, 0),
 140840720: (22, 0, 24, 0),
 140840732: (27, 0, 28, 0),
 140840744: (18, 0, 21, 0),
 140840756: (19, 0, 20, 0),
 140840768: (34, 0, 35, 1),
 140840780: (21, 0, 22, 0),
 140840792: (13, 0, 14, 0),
 140840804: (7, 0, 9, 0),
 140840816: (2, 0, 4, 0),
 140840828: (14, 0, 15, 0),
 140840840: (9, 0, 10, 0),
 140840852: (11, 0, 8, 0)},
                              elt_data=\
{2: {'caption': 'SEQUENCES',
     'hide': True,
     'lazy': True,
     'minimal': False,
     'port_hide_changed': set([]),
     'posx': 113.75,
     'posy': 86.25,
     'priority': 0},
 3: {'caption': 'Plot',
     'hide': True,
     'lazy': True,
     'minimal': False,
     'port_hide_changed': set([]),
     'posx': 385.0,
     'posy': 251.25,
     'priority': 0},
 4: {'caption': 'Cluster',
     'hide': True,
     'lazy': True,
     'minimal': False,
     'port_hide_changed': set([]),
     'posx': 140.0,
     'posy': 160.0,
     'priority': 0},
 5: {'caption': 'SelectVariable',
     'hide': True,
     'lazy': True,
     'minimal': False,
     'port_hide_changed': set([]),
     'posx': 125.0,
     'posy': 256.25,
     'priority': 0},
 6: {'caption': 'Plot',
     'hide': True,
     'lazy': True,
     'minimal': False,
     'port_hide_changed': set([]),
     'posx': 378.75,
     'posy': 178.75,
     'priority': 0},
 7: {'caption': 'Segmentation',
     'hide': True,
     'lazy': True,
     'minimal': False,
     'port_hide_changed': set([3, 4, 6, 7]),
     'posx': -48.75,
     'posy': 323.75,
     'priority': 0},
 8: {'caption': 'SelectVariable',
     'hide': True,
     'lazy': True,
     'minimal': False,
     'port_hide_changed': set([]),
     'posx': 201.25,
     'posy': 385.0,
     'priority': 0},
 9: {'caption': 'SelectVariable',
     'hide': True,
     'lazy': True,
     'minimal': False,
     'port_hide_changed': set([]),
     'posx': -23.75,
     'posy': 372.5,
     'priority': 0},
 10: {'caption': 'PlotData (gnuplot)',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': -35.0,
      'posy': 420.0,
      'priority': 0},
 11: {'caption': 'Segmentation',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([2, 4, 6, 7]),
      'posx': 173.75,
      'posy': 328.75,
      'priority': 0},
 12: {'caption': 'PlotData (gnuplot)',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': 188.75,
      'posy': 436.25,
      'priority': 0},
 13: {'caption': 'SegmentationSample',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': 363.75,
      'posy': 331.25,
      'priority': 0},
 14: {'caption': 'SelectIndividual',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': 411.25,
      'posy': 441.25,
      'priority': 0},
 15: {'caption': 'PlotData (gnuplot)',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': 403.75,
      'posy': 491.25,
      'priority': 0},
 16: {'caption': '4',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': 458.75,
      'posy': 371.25,
      'priority': 0},
 17: {'caption': '5',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': 505.0,
      'posy': 371.25,
      'priority': 0},
 18: {'caption': 'SegmentationSample',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': 572.5,
      'posy': 325.0,
      'priority': 0},
 19: {'caption': 'ComputeCorrelation multivariate',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': 760.0,
      'posy': 388.75,
      'priority': 0},
 20: {'caption': 'Plot (gnuplot)',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': 857.5,
      'posy': 443.75,
      'priority': 0},
 21: {'caption': 'SelectVariable',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': 578.75,
      'posy': 397.5,
      'priority': 0},
 22: {'caption': 'PointwiseAverage',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': 671.25,
      'posy': 507.5,
      'priority': 0},
 23: {'caption': 'PlotData (gnuplot)',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': 793.75,
      'posy': 617.5,
      'priority': 0},
 24: {'caption': 'SelectIndividual',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': 793.75,
      'posy': 568.75,
      'priority': 0},
 25: {'caption': 'PlotData (gnuplot)',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': 351.25,
      'posy': 71.25,
      'priority': 0},
 26: {'caption': 'Vectors',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': 655.0,
      'posy': 565.0,
      'priority': 0},
 27: {'caption': 'Regression',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': 518.75,
      'posy': 627.5,
      'priority': 0},
 28: {'caption': 'Plot (gnuplot)',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': 585.0,
      'posy': 681.25,
      'priority': 0},
 29: {'posx': 123.47222222222223,
      'posy': 0.69444444444445175,
      'txt': 'Source file'},
 30: {'posx': 641.25, 'posy': 72.5, 'txt': 'Packages : VPlants.Stat'},
 31: {'posx': 643.75, 'posy': 101.25, 'txt': 'Authors : Yann Guedon'},
 32: {'posx': 641.25,
      'posy': 127.5,
      'txt': 'Credits : Celine Meredieu, Yves Caraglio '},
 33: {'posx': 527.5,
      'posy': -22.5,
      'txt': 'Corsican pine tree trunks described at the annual shoot scale: \nGaussian change-point models'},
 34: {'caption': 'packagedir',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': 5.5555555555555465,
      'posy': -27.777777777777764,
      'priority': 0},
 35: {'caption': 'filename',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([1]),
      'posx': 8.3333333333333357,
      'posy': 22.222222222222229,
      'priority': 0},
 36: {'posx': -40.0,
      'posy': 472.5,
      'txt': 'Gaussian change-point\n model represented \nby a step function'},
 37: {'posx': 198.75, 'posy': 486.25, 'txt': 'Suboptimal\nsegmentation'},
 38: {'posx': 407.5, 'posy': 536.25, 'txt': 'Segmentation of\n2 individuals'},
 41: {'posx': 872.5,
      'posy': 481.25,
      'txt': 'Autocorrelation function\ncomputed from the \nresidual sequences'},
 42: {'posx': 391.25, 'posy': 116.25, 'txt': 'Input data'},
 43: {'posx': 526.25, 'posy': 185.0, 'txt': 'Bivariate change-point model'},
 44: {'posx': 535.0, 'posy': 251.25, 'txt': 'Univariate change-point model'},
 45: {'posx': 740.0,
      'posy': 676.25,
      'txt': 'Pointwise average\nreisual sequence'},
 '__in__': {'caption': 'In',
            'hide': True,
            'lazy': True,
            'minimal': False,
            'port_hide_changed': set([]),
            'posx': 20.0,
            'posy': 5.0,
            'priority': 0},
 '__out__': {'caption': 'Out',
             'hide': True,
             'lazy': True,
             'minimal': False,
             'port_hide_changed': set([]),
             'posx': 20.0,
             'posy': 250.0,
             'priority': 0}},
                              elt_value=\
{2: [(1, "'SEQUENCES'")],
 3: [(1, '2'), (2, '5'), (3, "'Numeric'"), (4, "'Segment'")],
 4: [(1, "'Step'"), (2, '1'), (3, '10'), (4, '0.0'), (5, '[None]')],
 5: [(1, '[1]'), (2, "'Keep'")],
 6: [(1, '5'), (2, '4'), (3, "'Numeric, Numeric'"), (4, "'Segment'")],
 7: [(1, '2'),
     (2, '10'),
     (3, 'None'),
     (4, "''"),
     (5, "'Numeric'"),
     (6, "'Estimated'"),
     (7, "'Sequence'")],
 8: [(1, '[2, 3]'), (2, "'Keep'")],
 9: [(1, '[2, 3]'), (2, "'Keep'")],
 10: [],
 11: [(1, '2'),
      (2, 'None'),
      (3, '[1936, 1943, 1961, 1986]'),
      (4, "''"),
      (5, "'Numeric'"),
      (6, "'Estimated'"),
      (7, "'Sequence'")],
 12: [],
 13: [(1, '[5, 6, 6, 4, 4, 4]'),
      (2, "''"),
      (3, "'Numeric'"),
      (4, "'Sequence'")],
 14: [(2, "'Keep'")],
 15: [],
 16: [(0, '4')],
 17: [(0, '5')],
 18: [(1, '[5, 6, 6, 4, 4, 4]'),
      (2, "''"),
      (3, "'Numeric'"),
      (4, "'Residual'")],
 19: [(1, 'True'),
      (2, '2'),
      (3, 'None'),
      (4, '20'),
      (5, "'Pearson'"),
      (6, "'Exact'")],
 20: [],
 21: [(1, '[2]'), (2, "'Keep'")],
 22: [(1, 'True'), (2, "'Sequence'"), (3, "''"), (4, "''"), (5, "'ASCII'")],
 23: [],
 24: [(1, '[0, 7]'), (2, "'Keep'")],
 25: [],
 26: [(1, 'False')],
 27: [(1, "'MovingAverage'"),
      (2, '1'),
      (3, '2'),
      (4, '[1]'),
      (5, '[]'),
      (6, 'None'),
      (7, '0.0'),
      (8, "'Averaging'"),
      (9, 'True')],
 28: [],
 29: [],
 30: [],
 31: [],
 32: [],
 33: [],
 34: [(0, "'Demo.ChangePoint'")],
 35: [(0, "'pin_laricio_7x.seq'")],
 36: [],
 37: [],
 38: [],
 41: [],
 42: [],
 43: [],
 44: [],
 45: [],
 '__in__': [],
 '__out__': []},
                              lazy=True,
                              )

    pkg.add_factory(nf)


    nf = CompositeNodeFactory(name='Dycorinia change point', 
                              description='Analysis of the successive internode lengthes of Dycorinia guinensis.', 
                              category='STAT',
                              doc='',
                              inputs=[],
                              outputs=[],
                              elt_factory=\
{2: ('vplants.stat', 'Load_from_file'),
 4: ('Catalog.Data', 'int'),
 6: ('vplants.stat', 'PlotSegmentProfile (gnuplot)'),
 7: ('vplants.stat', 'SelectVariable'),
 8: ('vplants.stat', 'SelectVariable'),
 9: ('vplants.stat', 'Segmentation'),
 10: ('vplants.stat', 'Segmentation'),
 11: ('Catalog.Data', 'string'),
 12: ('Catalog.Data', 'string'),
 13: ('vplants.stat', 'Segmentation'),
 14: ('Catalog.Data', 'string'),
 15: ('Catalog.Data', 'int'),
 16: ('vplants.stat', 'SelectVariable'),
 17: ('vplants.stat', 'Merge'),
 18: ('vplants.stat', 'PlotData (gnuplot)'),
 21: ('vplants.stat', 'Segmentation'),
 22: ('Catalog.Data', 'int'),
 23: ('Catalog.Data', 'int'),
 24: ('Catalog.Data', 'string'),
 25: ('vplants.stat', 'SelectVariable'),
 26: ('vplants.stat', 'PlotSegmentProfile (gnuplot)'),
 27: ('Catalog.Data', 'string'),
 28: ('vplants.stat', 'PlotSegmentProfile (gnuplot)'),
 29: ('Catalog.Data', 'string'),
 30: ('Catalog.Data', 'int'),
 31: ('Catalog.Data', 'packagedir'),
 32: ('Catalog.Data', 'filename'),
 33: ('System', 'annotation'),
 34: ('System', 'annotation'),
 35: ('System', 'annotation'),
 37: ('System', 'annotation'),
 39: ('System', 'annotation'),
 40: ('System', 'annotation'),
 41: ('System', 'annotation')},
                              elt_connections=\
{140840420: (30, 0, 6, 2),
 140840432: (31, 0, 32, 1),
 140840444: (17, 0, 18, 0),
 140840456: (2, 0, 9, 0),
 140840468: (22, 0, 28, 1),
 140840480: (27, 0, 26, 3),
 140840492: (2, 0, 28, 0),
 140840504: (25, 0, 26, 0),
 140840516: (7, 0, 17, 0),
 140840552: (12, 0, 10, 5),
 140840564: (9, 0, 8, 0),
 140840576: (23, 0, 28, 2),
 140840588: (15, 0, 13, 1),
 140840600: (8, 0, 17, 0),
 140840612: (16, 0, 17, 0),
 140840624: (32, 0, 2, 0),
 140840636: (24, 0, 21, 5),
 140840648: (21, 0, 25, 0),
 140840660: (24, 0, 28, 3),
 140840672: (15, 0, 10, 1),
 140840684: (14, 0, 13, 5),
 140840696: (29, 0, 6, 3),
 140840708: (15, 0, 9, 1),
 140840720: (10, 0, 7, 0),
 140840732: (22, 0, 21, 1),
 140840744: (2, 0, 10, 0),
 140840756: (23, 0, 21, 2),
 140840768: (2, 0, 21, 0),
 140840780: (11, 0, 9, 5),
 140840816: (2, 0, 13, 0),
 140840828: (2, 0, 6, 0),
 140840840: (13, 0, 16, 0),
 140840852: (4, 0, 6, 1)},
                              elt_data=\
{2: {'caption': 'SEQUENCES',
     'hide': True,
     'lazy': True,
     'minimal': False,
     'port_hide_changed': set([]),
     'posx': 183.75,
     'posy': 35.0,
     'priority': 0},
 4: {'caption': '1',
     'hide': True,
     'lazy': True,
     'minimal': False,
     'port_hide_changed': set([]),
     'posx': 466.25,
     'posy': 11.25,
     'priority': 0},
 6: {'caption': 'PlotSegmentProfile (gnuplot)',
     'hide': True,
     'lazy': True,
     'minimal': False,
     'port_hide_changed': set([]),
     'posx': 410.0,
     'posy': 70.0,
     'priority': 0},
 7: {'caption': 'SelectVariable',
     'hide': True,
     'lazy': True,
     'minimal': False,
     'port_hide_changed': set([2]),
     'posx': 296.25,
     'posy': 333.75,
     'priority': 0},
 8: {'caption': 'SelectVariable',
     'hide': True,
     'lazy': True,
     'minimal': False,
     'port_hide_changed': set([2]),
     'posx': 167.5,
     'posy': 335.0,
     'priority': 0},
 9: {'caption': 'Segmentation',
     'hide': True,
     'lazy': True,
     'minimal': False,
     'port_hide_changed': set([3, 4]),
     'posx': 123.75,
     'posy': 267.5,
     'priority': 0},
 10: {'caption': 'Segmentation',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([3, 4, 7]),
      'posx': 275.0,
      'posy': 267.5,
      'priority': 0},
 11: {'caption': "'Numeric'",
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': 192.5,
      'posy': 195.0,
      'priority': 0},
 12: {'caption': "'Mean'",
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': 323.75,
      'posy': 197.5,
      'priority': 0},
 13: {'caption': 'Segmentation',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([3, 4, 7]),
      'posx': 402.5,
      'posy': 263.75,
      'priority': 0},
 14: {'caption': "'Variance'",
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': 433.75,
      'posy': 198.75,
      'priority': 0},
 15: {'caption': '1',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': 292.5,
      'posy': 197.5,
      'priority': 0},
 16: {'caption': 'SelectVariable',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([2]),
      'posx': 421.25,
      'posy': 333.75,
      'priority': 0},
 17: {'caption': 'Merge',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': 327.5,
      'posy': 411.25,
      'priority': 0},
 18: {'caption': 'PlotData (gnuplot)',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': 290.0,
      'posy': 471.25,
      'priority': 0},
 21: {'caption': 'Segmentation',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([3, 4]),
      'posx': 582.5,
      'posy': 243.75,
      'priority': 0},
 22: {'caption': '1',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': 663.75,
      'posy': 137.5,
      'priority': 0},
 23: {'caption': '3',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': 716.25,
      'posy': 137.5,
      'priority': 0},
 24: {'caption': "'Mean'",
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': 761.25,
      'posy': 133.75,
      'priority': 0},
 25: {'caption': 'SelectVariable',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([2]),
      'posx': 615.0,
      'posy': 310.0,
      'priority': 0},
 26: {'caption': 'PlotSegmentProfile (gnuplot)',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': 640.0,
      'posy': 373.75,
      'priority': 0},
 27: {'caption': "'Variance'",
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': 762.5,
      'posy': 312.5,
      'priority': 0},
 28: {'caption': 'PlotSegmentProfile (gnuplot)',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': 755.0,
      'posy': 213.75,
      'priority': 0},
 29: {'caption': "'Numeric'",
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': 555.0,
      'posy': 7.5,
      'priority': 0},
 30: {'caption': '3',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': 508.75,
      'posy': 10.0,
      'priority': 0},
 31: {'caption': 'packagedir',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([]),
      'posx': 181.80555555555554,
      'posy': -85.277777777777771,
      'priority': 0},
 32: {'caption': 'filename',
      'hide': True,
      'lazy': True,
      'minimal': False,
      'port_hide_changed': set([1]),
      'posx': 184.58333333333334,
      'posy': -35.277777777777771,
      'priority': 0},
 33: {'posx': 412.5,
      'posy': -78.75,
      'txt': 'Dycorinia guianensis main axis\ndescribed at the internode scale:\nGuassian change point model'},
 34: {'posx': 831.25, 'posy': -48.75, 'txt': 'Author : Yann Guedon'},
 35: {'posx': 825.0, 'posy': -25.0, 'txt': ' Credits : Yves Caraglio'},
 37: {'posx': 262.5,
      'posy': 515.0,
      'txt': 'Comparison of the 3 Gaussian\nchange-point models'},
 39: {'posx': 791.25, 'posy': 252.5, 'txt': 'Change in the mean model'},
 40: {'posx': 665.0,
      'posy': 66.25,
      'txt': 'Change in the mean and \nthe variance model'},
 41: {'posx': 632.5, 'posy': 427.5, 'txt': 'Change in the the variance model'},
 '__in__': {'caption': 'In',
            'hide': True,
            'lazy': True,
            'minimal': False,
            'port_hide_changed': set([]),
            'posx': 20.0,
            'posy': 5.0,
            'priority': 0},
 '__out__': {'caption': 'Out',
             'hide': True,
             'lazy': True,
             'minimal': False,
             'port_hide_changed': set([]),
             'posx': 20.0,
             'posy': 250.0,
             'priority': 0}},
                              elt_value=\
{2: [(1, "'SEQUENCES'")],
 4: [(0, '1')],
 6: [(4, "'Segment'")],
 7: [(1, '[1]'), (2, "'Keep'")],
 8: [(1, '[1]'), (2, "'Keep'")],
 9: [(2, '3'), (3, '[]'), (4, "''"), (6, "'Fixed'"), (7, "'Sequence'")],
 10: [(2, '3'), (3, '[]'), (4, "''"), (6, "'Fixed'"), (7, "'Sequence'")],
 11: [(0, "'Numeric'")],
 12: [(0, "'Mean'")],
 13: [(2, '3'), (3, '[]'), (4, "''"), (6, "'Fixed'"), (7, "'Sequence'")],
 14: [(0, "'Variance'")],
 15: [(0, '1')],
 16: [(1, '[1]'), (2, "'Keep'")],
 17: [],
 18: [],
 21: [(3, '[]'), (4, "''"), (6, "'Fixed'"), (7, "'Residual'")],
 22: [(0, '1')],
 23: [(0, '3')],
 24: [(0, "'Mean'")],
 25: [(1, '[2]'), (2, "'Keep'")],
 26: [(1, '1'), (2, '3'), (4, "'Segment'")],
 27: [(0, "'Variance'")],
 28: [(4, "'Segment'")],
 29: [(0, "'Numeric'")],
 30: [(0, '3')],
 31: [(0, "'Demo.ChangePoint'")],
 32: [(0, "'angelique_internode_length.seq'")],
 33: [],
 34: [],
 35: [],
 37: [],
 39: [],
 40: [],
 41: [],
 '__in__': [],
 '__out__': []},
                              lazy=True,
                              )

    pkg.add_factory(nf)


    pkgmanager.add_package(pkg)

