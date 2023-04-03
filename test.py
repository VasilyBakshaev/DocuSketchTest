import unittest
from func import plot_drawer

class Test_plot_drawer(unittest.TestCase):
  def setUp(self):
    self.plot_drawer = plot_drawer()
  def test_add(self):
    self.assertEqual(self.plot_drawer.draw_plots('https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json'), ['plots/Name_to_mean_plot.png',
 'plots/Name_to_max_plot.png',
 'plots/Name_to_min_plot.png',
 'plots/Name_to_floor_mean_plot.png',
 'plots/Name_to_floor_max_plot.png',
 'plots/Name_to_floor_min_plot.png',
 'plots/Name_to_ceiling_mean_plot.png',
 'plots/Name_to_ceiling_max_plot.png',
 'plots/Name_to_ceiling_min_plot.png'])

if __name__ == "__main__":
  unittest.main()