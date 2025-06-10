# Principal Component Analysis (PCA) on Global Health Statistics

A comprehensive implementation of Principal Component Analysis from scratch using NumPy to analyze global health statistics data and reduce dimensionality while preserving key variance patterns.

ter notebook
```

## Dataset

The project uses the **Global Health Statistics** dataset from Kaggle:

- **Source**: Kaggle Dataset by malaiarasugraj
- **Size**: 1,000,000 records × 22 features
- **Features**: Health indicators including prevalence rates, mortality, healthcare access, economic factors
- **Download**: Automatically handled via kagglehub in the notebook

```python
import kagglehub

# Download latest version
path = kagglehub.dataset_download("malaiarasugraj/global-health-statistics")

print("Path to dataset files:", path)
```

## Usage

### Running the Analysis

1. Open the Jupyter notebook: `Untitled.ipynb`
2. Execute cells sequentially to:
   - Download and load the dataset
   - Preprocess numerical data
   - Implement PCA from scratch
   - Visualize results and analyze variance

### Key Results

- **Original dimensions**: 15 numerical features
- **Reduced dimensions**: 2 principal components
- **Variance explained**: Calculated for each component
- **Reconstruction error**: Measured via MSE
- **Visualizations**: Eigenvalue plots and PCA scatter plots

## Results

The PCA implementation successfully:
- Reduces 15-dimensional health data to 2 dimensions
- Preserves significant variance in the first few components
- Provides clear visualization of data structure
- Demonstrates effective dimensionality reduction with minimal information loss

Key findings:
- First few principal components capture majority of dataset variance
- Clear separation patterns visible in reduced dimensional space
- Reconstruction maintains essential data characteristics

## Technologies Used

- **Python 3.x** - Primary programming language
- **NumPy** - Numerical computations and linear algebra
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Data visualization and plotting
- **Kagglehub** - Dataset download and management
- **Jupyter Notebook** - Interactive development environment

## Project Structure

```
PCA/
├── Untitled.ipynb           # Main PCA implementation notebook
├── README.md               # Project documentation
├── Global Health Statistics.csv  # Dataset (downloaded via kagglehub)
└── requirements.txt        # Python dependencies (create if needed)
```

## Contributing

Contributions are welcome! Areas for improvement:
- Add more sophisticated visualization techniques
- Implement additional dimensionality reduction methods
- Include statistical significance tests
- Add interactive plotting capabilities

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/enhancement`)
3. Commit your changes (`git commit -m 'Add new visualization'`)
4. Push to the branch (`git push origin feature/enhancement`)
5. Open a Pull Request

