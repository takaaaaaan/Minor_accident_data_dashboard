$('.my-class').slick({
    // 既存のオプション
    dots: true,
    infinite: false,
    speed: 300,
    slidesToShow: 3,
    slidesToScroll: 3,
    // レスポンシブ設定
    responsive: [
        {
            breakpoint: 1024, // 1024px以下のビューポートサイズで
            settings: {
                slidesToShow: 3,
                slidesToScroll: 3,
                infinite: true,
                dots: true
            }
        },
        {
            breakpoint: 600, // 600px以下のビューポートサイズで
            settings: {
                slidesToShow: 2,
                slidesToScroll: 2
            }
        },
        {
            breakpoint: 480, // 480px以下のビューポートサイズで
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1
            }
        }
    ]
});