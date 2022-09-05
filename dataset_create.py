class MyDataset(Dataset):
    
    def __init__(self, nodes, feats, **kwargs):
        self.nodes = nodes
        self.feats = feats
        print('run1')
        super().__init__(**kwargs)


    # Create the directory
        print(self.path)
      #os.mkdir('/content/sample_data/custom_dataset' + str(self))

    # Write the data to file
        for i0 in range(0,249):
          x = mol_1_attr[i0]
          print(mol_1_attr[i0])
          a = [[0,1,1],[1,0,0],[1,0,0]]
          y = 1
          print('run2')
          filename = os.path.join('/content/sample_data/Output', f'graph_{i0}')
          np.savez(filename, x=x, a=a, y=y)

    def read(self):
    # We must return a list of Graph objects
      output = []

      for i01 in range(0,249):
        data = np.load(os.path.join('/content/sample_data/Output', f'graph_{i01}.npz'))
        output.append(
            Graph(x=data['x'], a=data['a'], y=data['y'])
        )

      return output