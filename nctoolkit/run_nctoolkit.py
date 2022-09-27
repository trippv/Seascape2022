import nctoolkit as nc
data = nc.open_data("$1")
bottom = nc.open_data("$1")
bottom.bottom_mask()
data.multiply(bottom)
data.vertical_sum()
data.to_nc("outfile.nc")
