// 파일 선택 이벤트 핸들러
function handleFileSelect(event) {
    const fileList = event.target.files; // 선택된 파일 목록을 가져오기
    
    // 선택된 파일들의 정보를 출력하거나 원하는 작업을 수행
    for (let i = 0; i < fileList.length; i++) {
      const file = fileList[i];
      console.log('선택된 파일:', file.name);
    }
  }
  
  // 파일 선택 버튼 요소를 가져오기
  const fileInput = document.getElementById('file-input');
  
  // 파일 선택 이벤트 리스너 등록
  fileInput.addEventListener('change', handleFileSelect);