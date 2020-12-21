import pandas as pd


movieData = pd.read_csv('data/movies.csv')
ratingData = pd.read_csv('data/ratings.csv')
tagsData = pd.read_csv('data/tags.csv')
linksData = pd.read_csv('data/links.csv')
genomeTagsData = pd.read_csv('data/genome-tags.csv')
genomeScoreData = pd.read_csv('data/genome-scores.csv')



def generateGenomeMatrix(moviesData, genomeScoresData):
	x = moviesData[['movieId', 'title']]
	y = genomeScoresData.pivot(index = 'movieId', columns = 'tagId', values = 'relevance')
	z = x.merge(y, how = 'left', on = 'movieId')
	z.to_csv('data/generatedGenomeMatrix.csv')


if __name__ == "__main__":
	generateGenomeMatrix(movieData, genomeScoreData)



