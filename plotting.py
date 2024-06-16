import numpy as np
import plotly.graph_objects as go

def plot_3d_slices(data, x_index=None, y_index=None, z_index=None):
    """
    Plots three orthogonal slices from a 3D dataset using Plotly.

    Parameters:
    - data: 3D numpy array.
    - x_index: Index along the x-axis for the vertical slice.
    - y_index: Index along the y-axis for the horizontal slice.
    - z_index: Index along the z-axis. Defaults to the middle of the dataset.

    Example:
    plot_3d_slices(flux_data, x_index=30, y_index=30, z_index=30)
    """
    if x_index is None:
        x_index = data.shape[0] // 2
    if y_index is None:
        y_index = data.shape[1] // 2
    if z_index is None:
        z_index = data.shape[2] // 2

    vmax = data.max()
    vmin = data.min()

    x = np.linspace(0, data.shape[0]-1, data.shape[0])
    y = np.linspace(0, data.shape[1]-1, data.shape[1])
    z = np.linspace(0, data.shape[2]-1, data.shape[2])
    X, Y, Z = np.meshgrid(x, y, z, indexing='ij')

    fig = go.Figure()

    # X-axis slice
    fig.add_trace(go.Surface(z=Z[x_index, :, :], x=X[x_index, :, :], y=Y[x_index, :, :],
                             surfacecolor=data[x_index, :, :], colorscale='Turbo',
                             cmin=vmin, cmax=vmax, showscale=False))

    # Y-axis slice
    fig.add_trace(go.Surface(z=Z[:, y_index, :], x=X[:, y_index, :], y=Y[:, y_index, :],
                            surfacecolor= data[:, y_index, :], colorscale='Turbo',
                            cmin=vmin, cmax=vmax, showscale=False))

    # Z-axis slice
    fig.add_trace(go.Surface(x=X[:, :, z_index], y=Y[:, :, z_index], z=Z[:, :, z_index],
                             surfacecolor= data[:, :, z_index], colorscale='Turbo',
                             cmin=vmin, cmax=vmax, showscale=True))

    fig.update_layout(
        title="3D Surface Slices of Logarithmic Data",
        autosize=False,
        width=800,
        height=800,
        scene=dict(
            xaxis_title='X axis',
            yaxis_title='Y axis',
            zaxis_title='Z axis'
        )
    )

    fig.show()

def plot_mesh(nodes, faces, color='blue', x_min=None, y_min=None, z_min=None):
    fig = go.Figure()

    # Apply filters on nodes and adjust faces accordingly
    valid_nodes_mask = np.ones(len(nodes), dtype=bool)
    if x_min is not None:
        valid_nodes_mask &= (nodes[:, 0] > x_min)
    if y_min is not None:
        valid_nodes_mask &= (nodes[:, 1] > y_min)
    if z_min is not None:
        valid_nodes_mask &= (nodes[:, 2] > z_min)

    valid_nodes = np.where(valid_nodes_mask)[0]
    node_index_map = {old_index: new_index for new_index, old_index in enumerate(valid_nodes)}
    nodes = nodes[valid_nodes]

    mask = np.all(np.isin(faces, valid_nodes), axis=1)
    faces = faces[mask]
    for i in range(faces.shape[1]):
        faces[:, i] = [node_index_map[idx] for idx in faces[:, i]]

    # Add faces
    fig.add_trace(go.Mesh3d(x=nodes[:, 0], y=nodes[:, 1], z=nodes[:, 2],
                            i=faces[:, 0], j=faces[:, 1], k=faces[:, 2],
                            color=color, opacity=1))

    # Add edges
    for face in faces:
        for i in range(3): 
            start, end = face[i], face[(i + 1) % 3]
            fig.add_trace(go.Scatter3d(
                x=[nodes[start, 0], nodes[end, 0]],
                y=[nodes[start, 1], nodes[end, 1]],
                z=[nodes[start, 2], nodes[end, 2]],
                mode='lines',
                line=dict(color='black', width=2),
                showlegend=False
            ))

    fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
                      width=700, height=700, margin=dict(r=20, l=10, b=10, t=10))
    fig.show()
