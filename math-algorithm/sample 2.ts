const onChangeStartAtHandler = (startAt: Date | null) => {
  // startAt更新処理
};

const onChangeEndAtHandler = (endAt: Date | null) => {
  // endAt更新処理
};

type DateType = 'startAt' | 'endAt';

const onChangeDateHandler = (date: Date | null, dateType: DateType) => {
  dateType === 'startAt'
    ? console.log(date) // startAt更新処理
    : console.log(date); // endAt更新処理
};
