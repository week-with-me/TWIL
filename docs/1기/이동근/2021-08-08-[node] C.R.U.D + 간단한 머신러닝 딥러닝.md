tweeter의 클론 코딩을 하면서 C.R.U.D 를 만들어 보았다. 파일 구조는 MVC패턴의 형태로 만들었으며 M의 db, V의 router, c의 controller로 만들었습니다. 그리고 app.js로 서버를 실행 시켰습니다.

## C.R.U.D
### Database 에서의 C.R.U.D
#### POST구현
첫번째로 메모리에 POST기능 구현하기
```js
export async function create(text, userId) {
    const tweet = {
        id: Data.now().toString(),
        text,
        createdAt: new Date(),
        username
    };
}
```
두 번째로 orm을 사용하지 않고, mysql에 데이터 저장하기
```js
export async function create(text, userId) {
    return db.execute(
        'INSERT INTO tweets (text, createdAt, UserID) VALUE(?,?,?)', [text, new Date(), userId]
    );
}
```
sql 문을 통해서 직접 create 해줄 수 있다.

세 번째 sequelize를 사용하기
node.js에서 사용되어지는 대표적인 orm으로

```js
const Tweet = sequelize.define('tweet', {
    id: {
        type: DataTypes.INTEGER,
        autoIncrement: true,
        allowNull: false,
        primaryKey: true
    },
    text: {
        type: DataTypes.TEXT,
        allowNull: false
    }
})
Tweet.belongsTo(User);
```
mysql에서의 tweet이라는 테이블 명을 지정해준뒤 id, text와 같은 column을 지정해준다. 그리고

```js
export async function create(text, userId) {
    return Tweet.create({text, userId})
}
```
이런식으로만 적어주면 끝이 나게 된다.

#### GET
메모리 상에서 GET 구현하기
```js
export async function getAll() {
    return Promise.all(
        tweets.map(async (tweet) => {
            const {username, name, url} = await userRepository.findById(
                tweet.userId
            );
            return {...tweet, username, name};
        })
    );
};
```
orm 없이 GET 구현하기
```js
export async function getAll() {
    return db.execute( `SELECT tw.id, tw.text, tw.createdAt, tw.userId ,us.username, us.name FROM tweets as tw JOIN users as us on tw.userId=us.id ORDER BY tw.createdAt DESC`)
};
```
조건을 걸어서 구현하고 싶으먄
```js
return db.execute(`${SELECT_JOIN} WHERE tw.id=? ${ORDER_DESC}`, [id] ).then((result) => result[0][0])
```
보여지듯이 WHERE를 사용해서 SQL문에 조건을 걸어주면 된다.

orm으로 GET구현하기
```js
export async function getAll(){
    return Tweet.findAll({...INCLUDE_USER, ...ORDER_DESC, });   
};
```
만약 조건을 걸어서 구하고 싶으면
```js
export async function getById(id) {
    return Tweet.findOne({
        where: { id },
        ...INCLUDE_USER,
    })

```
Where을 통해 조건을 걸어주면 된다.

#### DELETE, UPDATE
삭제와 업데이트는 비슷하다
첫번째 메모리 상에서 실행
```js
// update
export function update(id, text) {
    const tweet = tweets.find((tweet) => tweet.id === id);
    if (tweet) {
        tweet.text = text;
    };
    return getById(tweet.id);
}

// delete
export function remove (id) {
    const tweet = tweets.filter(t => t.id !== id);
}
```
delete는 함수명과 똑같기 때문에 delete를 사용하게 되면 오류가 나게 된다 그래서 함수명을 remove로 해주었습니다.

orm을 사용하지 않기
```js
// update
export function update(id, text) {
    return db.execute.apply('UPDATE tweets SET text=? WHERE id=?', [text, id])
    .then(() => getById(id));
}

//delete
export function remove (id) {
    return db.execute('DELETE FROM tweets WHERE id=?', [id])
```

orm 사용한 후
```js
// update
export function update(id, text) {
    return Tweet.findByPk(id, INCLUDE_USER)//
    .then(tweet => {
        tweet.text = text;
        return tweet.save();
    })
}

// delete
export function remove (id) {
    return Tweet.findByPk(id, INCLUDE_USER)
    .then(tweet => {
        tweet.text = text;
        return tweet.destroy();
    })
}
```
이렇게 메모리에서의 C.R.U.D orm을 사용했을때 안했을 때 의 코드를 살펴 보았습니다.

----
## 간단한 머신러닝 딥러닝 용어
합성곱 신경망

## convolution Layer
-> 내가 찾고자 하는 패턴을 찾는 과정
padding 원본 이미지의 상하좌우에 한 줄 씩 추가
striding - 한번에 얼마나 움직일 것인지 적용할 것인가

## Pooling Layer
Max Pooling을 많이 쓰는것 같다
convolution Layer를 통해 filter 가 적용이 되었을때 이미지의 왜곡의 영향(노이즈)를 축소하는 과정

Max Pooling을 하면 내가 원하는 것을 찾는 도중에도 데이터의 사이즈가 커지지 않는 것을 의미한다.


## Fully Connected layer
우리가 알고 있는 뉴런 네트워크학이다. convolution Layer와 Pooling Layer를 통해 얻은 특징을 통해 이미지를 분류하는 것을 의미 한다.

마지막에는 softmax를 사용하는데 얻은 확률값 중 가장 큰 값을 얻는 것을 softmax 이다.


정리
- convolution Layer는 특징을 찾아내고, pooling  Layer는 convolution Layer가 이루어 질때 커졌던 데이터를 줄여가면서 처리할 맵의 크기를 줄여준다. 이를 N번 반복한다. 
- 영역의 크기는 작아졌기 때문에 빠른 학습이 가능하다.

### CNN(합성곱 신경망 기반의 다양한 이미지 처리 기술)
#### Object detection & segmentation
노트북은 여기 이 바운딩 박스 안에 있다. 바운딩 박스를 찾으면서 세그멘테이션을 이루었다. 라고 하는 것 
#### SR(Super Resolution)
저화질을 고화질로 바꿔 주는 작업

### 워드 임베딩(Word Embedding)
단어를 추출 했으면 어떻게 숫자로 표현할 것인가? 
비정형 데이터를 정형 데이터로 바꿔주는 것

#### count-based Representations
Bag of Words
one-hot encoding
Document term matrix
->단어가 몇 번이냐 쓰이냐

#### Distributed Representations
word2vec : word embedding

#### Bag of words
bag of words는 예전부터 쓰여왔지만 word embedding 보다 좋지 않아서 현재는 많이 쓰이지 않는다.

자연어 데이터
['안녕','만나서','반가워']
['안녕','나도','반가워']

bag of words
['안녕','만나서', '반가워', '나도']

자연어 데이터에서 unique한 단어가 나온가는 것이 bag of words 이다.

one-hot vector
[1,1,1,0] [1,1,1,1]
학습 데이터의 모든 토큰을 크기로 한 벡터에서 해당 문장에 토큰이 존재하는지 확인

Document term matrix
정부가 발표하는 물가상승률과 소비자가 느끼는 물가 상승률은 다르다
('정부': 0, '가': 1, '발표':2, '하는':3, '물가상승률':4,'과': 5, '소비자':6, '느끼는': 7, '은':8, '다르다': 9)

[1,2,1,1,2,1,1,1,1,1,]
one hot encoding 결과에 빈도수 정보를 추가

### Word2vec
단어들을 의미상으로 유사한 단어가 벡터공간에 가까이 있도록 Mapping 시키는 작업을 의미  특정 함수를 통해 우리가 원하는 차원으로 단어의 벡터를 Emdedding함

단어들의 연관성을 표현하기 위해서 나온 것이 워드 임베딩

내가 어떻게 해야 그대를 잊을 수 있을까

-- tokenizing

'내','가', '어떻게', '해야', '그대', '를', '잊을', '수' '있을', '까'

작업후 주변 단어가 어떤 것이 나올지 nuranize?를 통해 예측을 하게 한다.

비슷한 단어는 비슷한 맥락에서 나오기때문에 
주변 단어로 중심단어를 예측하도록 학습

단순히 단어가 몇 번 나왔는지로 예측하는 것이 아니라, 주변으로 판단하기 때문에 엄마라는 단어를 통해 학습을 하더라도 아빠와 관련되도록 예측해 유사한 다큐먼츠(그룹)이라고 알 수 있다.
