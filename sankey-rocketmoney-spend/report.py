from collections import namedtuple
from typing import List, TypedDict
import plotly.graph_objects as go

class Datapoint(TypedDict):
    source: str
    target: str
    value: float

def create_sankey_diagram(data_points: List[Datapoint]) -> None:
    # Extract unique nodes from the data
    nodes = list(set([dp['source'] for dp in data_points] + [dp['target'] for dp in data_points]))

    # Create dictionaries to map nodes to indices
    node_indices = {node: i for i, node in enumerate(nodes)}

    # Convert data_points to the format needed for the Sankey diagram
    link_source = [node_indices[dp['source']] for dp in data_points]
    link_target = [node_indices[dp['target']] for dp in data_points]
    values = [dp['value'] for dp in data_points]

    # Create Sankey diagram
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color='black', width=0.5),
            label=nodes
        ),
        link=dict(
            source=link_source,
            target=link_target,
            value=values
        )
    )])

    # Update layout for better aesthetics
    fig.update_layout(title_text="Sankey Diagram Example", font_size=10)
    fig.show()

if __name__ == '__main__':
  # Example usage
  data_points_example: List[Datapoint] = [
      {'source': 'Node A', 'target': 'Node B', 'value': 10},
      {'source': 'Node A', 'target': 'Node C', 'value': 15},
      {'source': 'Node B', 'target': 'Node C', 'value': 5},
      {'source': 'Node C', 'target': 'Node A', 'value': 12},
  ]

  create_sankey_diagram(data_points_example)
