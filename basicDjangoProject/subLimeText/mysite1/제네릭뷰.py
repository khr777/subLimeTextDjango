# Django에서 제공해주는 기본 클래스(파이썬이 아닌)
[ 제네릭 뷰 ]
웹 프로그램 개발시에 공통적으로 사용하는 로직을 미리 만들어 놓고 장고에서는 이것을
기본 클래스로 제공한다. 이때 이 클래스를 제네릭 뷰라고 한다.

그러면 개발자는 자신의 로직에 맞는 뷰를 선택해서 사용할 수 있다.

- 제네릭 뷰의 분류 : 
	Base View, Generic Display View, Generic Edit View, Generic Date View,

	* BaseView 
	- View : 가장 기본이되는 최상위 뷰, 다른 모든 제네릭 뷰들은 View의 하위 클래스 
	(다른 모든 뷰들이 기본적으로 View를 상속 받고 있다.)
	- TemplateView : 템플릿이 주어지면 해당 템플릿을 렌더링 해준다.
	- RedirectView : URL이 주어지면 해당 URL로 리다이렉트 시켜준다. 


	* Generic Display View
	- DetailView : 한 객체에 대한 상세한 정보를 보여준다.
	- ListView : 조건에 맞는 여러 개의 객체를 보여준다.

	* Generic Edit View 
	- FormView : 폼이 주어지면 해당 폼을 보여주는 뷰 
	- CreateView : 객체를 생성하는 폼을 보여주는 뷰
	- UpdateView : 기존 객체를 수정하는 폼을 보여주는 뷰
	- DeleteView : 	기존 객체를 삭제하는 폼을 보여주는 뷰


	* Generic Date View
	- YearArchiveView : 년도에 해당하는 객체를 보여주는 뷰
	- MonthArchiveView : 년도와 월이 주어지면 그에 해당하는 객체들을 보여주는 뷰
	- WeekArchiveView : 연도와 week가 주어지면 그에 해당하는 객체들을 보여주는 뷰

	- DayArchiveView : 연, 월, 일이 주어지면 그날짜에 해당하는 객체들을 보여주는 뷰
	- TodayArchiveView : 오늘 날짜에 해당하는 객체들을 보여주는 뷰
	- DateDetailView : 연, 월, 일 기본 키(또는 슬러그)가 주어지면 그에 해당하는 특정 객체 하나에 대한 
	 					상세한 정보를 보여주는 뷰


