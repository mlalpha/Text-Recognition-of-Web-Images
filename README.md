# ICPR 2018 CHALLENGE 1

# Text Recognition of Web Images

## 1. Introduction

  In the Internet world, pictures are important media for transmitting information, especially in the fields of e-commerce, social networking, and search. Everyday there are hundreds of trillion level images in flow communication. The text recognition in the picture has an important application value in the business field. It is the basic communication way of data information between online and offline, and it is also a hot spot in the academic circle. However, there is no OCR data set given first place to Chinese character and based network picture. This competition will publish web-based photo datasets. The datasets contain Chinese and English characters, covering dozens of typefaces, several to hundreds of pixels, multiple formats, and more interference backgrounds. It is expected that the academic community can do in-depth research on these data sets, and the industry can develop the AI field in the field of picture control, search, information entry and so on.
  
## 2. The Data Set

We provide 20000 images for this competition, of which 50% is for training, and 50% is for testing. The data sets are all derived from the network images, mainly composed of synthetic images, product description, and network advertising. A typical picture is shown in Figure 1.

| Document                                | Format        |
| --------------------------------------- |:-------------:|
| ICPR_text_train_part1_20180211.zip      | [.zip (193MB)](http://aliyuntianchiresult.cn-hangzhou.oss.aliyun-inc.com/file/race/documents/231650/ICPR_text_train_part1_20180211.zip?Expires=1519733725&OSSAccessKeyId=2zep9f8tkzg6ennfl26ciifi&Signature=KHmW%2FMuW4LdnYCkq%2BQwGhQeVaSE%3D&response-content-disposition=attachment%3B%20)  |

![Figure 1](https://work.alibaba-inc.com/aliwork_tfs/g01_alibaba-inc_com/tfscom/TB1fz1tXY9YBuNjy0FgXXcxcXXa.tfsprivate.png)

Figure 1: typical pictures

These images are the most common types of images on the network. Each image contains either complex typesetting, intensive small text, multilingual text, or watermark, which challenges text detection and recognition.

For each image, there is a corresponding text file（.txt）（UTF-8 Encoding and name：[Image file name] .txt）. A text file is a comma - separated file, in which each line corresponds to a text string in the image and has the following format：

X1，Y1，X2，Y2，X3，Y3，X4，Y4，“text”

Among X1，Y1，Y2，X2，X3，X4，Y3，Y4 it represents the four vertex coordinates of the outer quadrilateral of the text respectively. And "text" is the actual text content that the quadrangle contains.

     Figure 2 is an annotated picture, and a red box represents a tagged text box.

Figure 3 is a text file for annotated pictures. We mark the outer box for all languages and all the obscure text strings（For example, in Figure 2） with annotation. But for obscure text strings and other languages except Chinese and English, we use "###" instead of annotation.

![Figure 2](https://work.alibaba-inc.com/aliwork_tfs/g01_alibaba-inc_com/tfscom/TB1cnOqXVuWBuNjSspnXXX1NVXa.tfsprivate.png)


Figure 2：image.jpg

![Figure 3](https://work.alibaba-inc.com/aliwork_tfs/g01_alibaba-inc_com/tfscom/TB1qF1sX7yWBuNjy0FpXXassXXa.tfsprivate.png)

Figure 3：image.txt

## 3. Task Description

The network image text recognition:

To evaluate the performance of text recognition, the training model can only be trained with the training set provided.Extra data is not allowed. Fine-tuning models are also not allowed.

Training set:

Only Chinese, English and symbols are considered.（Ignore the rows which contain “###” after the last comma in the [image file name].txt.）

Test set:

Input: A text line picture.

Output: Put the recognition result to the corresponding [image file name].txt.

Submission:

All images corresponding to the [image file name].txt are put in a zip compression package and then submitted.

## 4. Evaluation criteria

  We will rank the results according to the total matching and Levenshtein distance respectively, but the final awards is assigned according to the ranking of Levenshtein distance.

