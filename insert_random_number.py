import sublime, sublime_plugin, random

class InsertRandomNumberCommand(sublime_plugin.TextCommand):
    def run(self, edit, start=0, end=100, precision=-1):
		for region in self.view.sel():
			rng = self.generate(start, end, precision)
			s_rng = str(rng) if (precision == 0) else format(rng, ".{0}f".format(precision))

			if region.empty():
				self.view.insert(edit, region.a, s_rng)
			else:
				self.view.replace(edit, region, s_rng)

	def generate(self, start=0, end=100, precision=-1):
		rng = random.uniform(start, end)

		if (precision > 0):
			rng = round(rng, precision)
		elif (precision == 0):
			rng = int(rng)

		return rng