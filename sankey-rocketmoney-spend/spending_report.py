from sankey import Datapoint, create_sankey_diagram
from secrets.spending23_full import datapoints

def main():
  print(datapoints)
  create_sankey_diagram(datapoints)

main()