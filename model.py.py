from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def scale_features(df):
    X = df[['Annual Income (k$)', 'Spending Score (1-100)']]
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return X_scaled


def find_wcss(X_scaled):
    wcss = []
    
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i)
        kmeans.fit(X_scaled)
        wcss.append(kmeans.inertia_)
    
    return wcss


def apply_kmeans(df, X_scaled, n_clusters=5):
    kmeans = KMeans(n_clusters=n_clusters)
    df['Cluster'] = kmeans.fit_predict(X_scaled)
    
    return df