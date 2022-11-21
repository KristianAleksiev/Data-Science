"""
1. Image processing - PIL library, scikit-image (skimage)
- Reading, exploring, manipulation
jpg format - 3 Channels
- Convolution (cross-correlation) - mixing the img(matrix) with small matrix
Result is another image

- Morphology - forms
Main morphology operations:
-- Dilation - replace all values with the max value
-- Erosion - replace all values with the min value
-- Opening - erosion followed by dilation
-- Closing - dilation followed by erosion
2. Text processing
nltk library - stopwords

- Text preparation
Normalization, tokenization, stopwords processing, stemming(lematization) in some cases

- Frequency analysis:
Most used symbols, distribution

- TF - IDF - Pre-processing algorithm for text specific stopwords
"""