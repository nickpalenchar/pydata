from typing import List, TypedDict, Union
import plotly.graph_objects as go
from pprint import pprint


class Datapoint(TypedDict):
    source: str
    target: str
    value: Union[float, str]

def calculate_autoout_value(data_points: List[Datapoint], dp: Datapoint) -> float:
    # Calculate the total value of all other datapoints with the same source
    total = 0
    for other_dp in data_points:
        if dp['target'] == other_dp['source']:
            if isinstance(other_dp['value'], int):
                total += other_dp['value']
            elif dp != other_dp and isinstance(other_dp['value'], str):
                if other_dp['value'] == 'autoout':
                    total += calculate_autoout_value(data_points, other_dp)
                else:
                    raise ValueError('Unknown value name')
            
    # total_value = sum(other_dp['value'] for other_dp in data_points 
    #     if dp['target'] == other_dp['source'] 
    #     and isinstance(other_dp['value'], int)
    # )
    return total

def calculate_autoin_value():
    pass # TODO

def process_datapoints(data_points: List[Datapoint]) -> List[Datapoint]:
    processed_data_points = []
    for dp in data_points:
        if dp['value'] == 'autoout':
            dp['value'] = calculate_autoout_value(data_points, dp)
        processed_data_points.append(dp)
    return processed_data_points

def create_sankey_diagram(data_points: List[Datapoint]) -> None:
    data_points = process_datapoints(data_points)
    pprint(data_points)

    nodes = list(set([dp['source'] for dp in data_points] + [dp['target'] for dp in data_points]))

    node_indices = {node: i for i, node in enumerate(nodes)}

    # Convert data_points to the format needed for the Sankey diagram
    link_source = [node_indices[dp['source']] for dp in data_points]
    link_target = [node_indices[dp['target']] for dp in data_points]
    values = [dp['value'] for dp in data_points]

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

    fig.update_layout(title_text="Sankey Diagram Example", font_size=10)
    fig.show()

# Example usage
data_points_example: List[Datapoint] = [
    {'source': 'Node A', 'target': 'Node B', 'value': 10},
    {'source': 'Node A', 'target': 'Node C', 'value': 15},
    {'source': 'Node B', 'target': 'Node C', 'value': 5},
    {'source': 'Node B', 'target': 'Node D', 'value': 8},
    {'source': 'Node C', 'target': 'Node A', 'value': 12},
    {'source': 'Node C', 'target': 'Node D', 'value': 3},
    {'source': 'Node D', 'target': 'Node C', 'value': 'autoout'},
]

if __name__ == '__main__':
    create_sankey_diagram(data_points_example)
