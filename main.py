from dash import Dash, html, dcc, Input, Output,State
import dash_bootstrap_components as dbc
import pickle
from func import make_map
import numpy as np
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.LUX],
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}], # USE TO DISPLAY ON MOBILEPHOBE
    url_base_pathname='/',
    )
server = app.server
app.title = "台南租屋估價系統"
town_vill=['中西區','北區','南區','安南區','安平區','東區','永康區']

all_vill=['三合里','三民里','中樓里','中興里','中華里','中西里','二王里','五條港里','五王里','仁和里','仁德里','仁愛里','佃東里','佃西里',
	'佛壇里','億載里','元寶里','元美里','光復里','光明里','光賢里','兌悅里','公園里','公塭里','公親里','六合里','再興里','力行里',
    '勝利里','北灣里','北興里','北華里','北門里','南廠里','南灣里','南美里','南聖里','南華里','南都里','南門里','原佃里','合興里',
    '和平里','和順里','國宅里','國安里','國平里','圍下里','城北里','城東里','城隍里','埔園里','塩洲里','塩田里','塩興里','塩行里',
    '塭南里','大光里','大同里','大和里','大學里','大安里','大德里','大忠里','大恩里','大成里','大智里','大林里','大橋里','大涼里',
    '大港里','大灣里','大福里','大興里','大豐里','天妃里','太子里','學東里','安和里','安富里','安康里','安慶里','安西里','安順里',
    '富強里','富裕里','小北里','小東里','小西門里','尚頂里','崇信里','崇善里','崇學里','崇德里','崇成里','崇文里','崇明里','崇誨里',
    '崑山里','州北里','州南里','平安里','平通里','幸福里','府前里','府南里','廣州里','建國里','建平里','彰南里','後甲里','復國里',
    '復興里','復華里','德光里','德高里','忠孝里','怡平里','成功里','成大里','成德里','振興里','文元里','文南里','文平里','文成里',
    '文聖里','文華里','新昌里','新東里','新樹里','新生里','新興里','新順里','明亮里','明德里','明興里','東光里','東和里','東安里',
    '東明里','東智里','東橋里','東灣里','東聖里','東興里','東門里','梅花里','正強里','正覺里','永寧里','永康里','永明里','永祥里',
    '永華里','泉南里','法華里','海佃里','海南里','海東里','海西里','淵中里','淵東里','淵西里','淺草里','溪北里','溪墘里','溪心里',
    '溪東里','溪頂里','烏竹里','王城里','王行里','理想里','田寮里','甲頂里','省躬里','砂崙里','神洲里','福德里','立人里','竹溪里',
    '網寮里','育平里','自強里','興農里','莊敬里','華平里','華德里','蔦松里','藥王里','虎尾里','衛國里','裕聖里','裕農里','西勢里',
    '西和里','西橋里','西湖里','西灣里','西賢里','賢北里','赤嵌里','路東里','郡南里','郡王里','重興里','金城里','金華里','長勝里',
    '長安里','長興里','開元里','開南里','開山里','關聖里','雙安里','頂安里','鳳凰里','鹽埕里','龍埔里','龍山里','龍潭里']

yk_vill=['龍埔里', '北興里', '塩興里', '永明里', '二王里', '安康里', '東橋里', '三合里', '六合里', '正強里', 
    '復華里', '尚頂里', '西橋里', '中華里', '西勢里', '神洲里', '建國里', '復國里', '龍潭里', '勝利里', '中興里', 
    '成功里', '塩洲里', '光復里', '大灣里', '甲頂里', '塩行里', '崑山里', '南灣里', '西灣里', '東灣里', '復興里',
    '新樹里', '北灣里', '五王里', '大橋里', '埔園里', '永康里', '網寮里', '三民里', '蔦松里', '烏竹里', '王行里']

zhxi_vill=['光賢里', '藥王里', '開山里', '永華里', '郡王里', '赤嵌里', '法華里', '五條港里', '小西門里', '南門里',
    '南美里', '南廠里', '府前里', '淺草里', '兌悅里', '西和里', '大涼里', '西賢里', '西湖里', '城隍里']

dong_vill=['成大里', '南聖里', '裕聖里', '復興里', '崇文里', '文聖里', '東智里', '崇德里', '東明里', '崇誨里', 
    '崇信里', '東門里', '崇成里', '東聖里', '德光里', '大同里', '小東里', '圍下里', '富強里', '德高里', '虎尾里', 
    '龍山里', '大學里', '忠孝里', '大福里', '莊敬里', '東安里', '中西里', '路東里', '和平里', '自強里', '崇明里', 
    '崇善里', '衛國里', '關聖里', '大德里', '崇學里', '大智里', '裕農里', '富裕里', '東光里', '後甲里', '仁和里', 
    '泉南里', '新東里']

nan_vill=['大林里', '佛壇里', '再興里', '新生里', '大恩里', '大忠里', '南都里', '金華里', '文華里', '明興里',
    '喜東里', '明亮里', '光明里', '興農里', '省躬里', '喜南里', '喜北里', '同安里', '明德里', '竹溪里', '新興里',
    '新昌里', '廣州里', '大成里', '國宅里', '田寮里', '鹽埕里', '建南里', '彰南里', '開南里', '鯤鯓里', '文南里',
    '府南里', '郡南里', '南華里', '永寧里', '松安里']

ba_vill=['福德里', '華德里', '北華里', '長興里', '元美里', '雙安里', '立人里', '大和里', '文成里', '成德里',
    '北門里', '合興里', '長勝里', '賢北里', '大興里', '大光里', '小北里', '公園里', '中樓里', '永祥里', '元寶里',
    '和順里', '成功里', '正覺里', '大港里', '文元里', '重興里', '大豐里', '開元里', '力行里', '東興里', '仁愛里',
    '振興里']

anping_vill=['育平里', '國平里', '平安里', '億載里', '王城里', '天妃里', '漁光里', '金城里', '平通里', '華平里',
    '怡平里', '建平里', '文平里']

annan_vill=['佃西里', '佃東里', '淵西里', '淵東里', '城東里', '學東里', '南興里', '公塭里', '城中里', '城北里',
    '總頭里', '原佃里', '新順里', '海西里', '海東里', '公親里', '長安里', '塩田里', '溪心里', '海南里', '東和里',
    '州北里', '州南里', '塭南里', '安順里', '安慶里', '頂安里', '安西里', '安東里', '媽祖宮里', '大安里', '安富里',
    '海佃里', '溪墘里', '理想里', '梅花里', '鳳凰里', '幸福里', '國安里', '布袋里', '淵中里', '溪東里', '城南里',
    '砂崙里', '青草里', '城西里', '溪北里', '安和里', '四草里', '鹿耳里', '溪頂里']



def bool2int(x):
    if x=='是' or x=='有' or x=='可':
        return [0,1]
    elif x=='否' or x=='無' or x=='不可':
        return [1,0]

lr=open('linearregression2.pickle','rb')
lr_model=pickle.load(lr)
rd=open('rd10002.pickle','rb')
rd_model=pickle.load(rd)
xgb=open('xgb10002.pickle','rb')
xgb_model=pickle.load(xgb)

app.layout=html.Div([
    dbc.Row([
        dbc.Col(
            children=[
                html.H1(
                    ["台南市區租屋估價平台"],
                    className='mx-3'
                )
            ],
            width=7,
            class_name='p-3'
        ),
        dbc.Col([
            html.H4(['預測模型選擇']),
            dcc.RadioItems(
                id='model-selection',
                options=['線性迴歸','隨機迴歸森林','極限梯度提升法'],
                value='極限梯度提升法',
                inline=True,
                inputClassName='mx-1',
                labelClassName='me-2',
            )
        ],width=5,className='p-2'),
    ]),
    dbc.Row([
        dbc.Col(
            children=[
            html.Div(
                id='map-part',
            ),
            html.Div(
                children=[
                    html.P(id='predict-money'),
                ],
                className='text-end fw-bold text-danger',
            )
        ],width=7),
        dbc.Col([
            html.Div([
                html.H4(['物件基本資訊']),
                dbc.Row([
                    dbc.Col([
                        html.Label(['鄉鎮市區']),
                        dcc.Dropdown(
                            id='x-district',
                            options=['東區','中西區','南區','北區','安平區','安南區','永康區'],
                            value='東區'
                        ),
                    ],width=6),
                    dbc.Col([
                        html.Label(['村里']),
                        dcc.Dropdown(
                            id='x-vill',
                            options=dong_vill,
                            value='大學里',
                        ),
                    ],width=6)
                ]),
                html.Br(),
                html.H4(['物件硬體資訊']),
                dbc.Row([
                    dbc.Col([
                        html.Label(['建築類型']),
                        dcc.Dropdown(
                            id='x-building-type',
                            options=['透天','公寓','電梯大樓'],
                            value='透天'
                        ),
                    ],width=4),
                    dbc.Col([
                        html.Label(['物件類型']),
                        dcc.Dropdown(
                            id='x-room-type',
                            options=['雅房','分租套房','獨立套房','整層住家'],
                            value='雅房'
                        ),
                    ],width=4),
                    dbc.Col([
                        html.Label(['提供車位']),
                        dcc.RadioItems(
                            id='x-parking',
                            options=['是','否'],
                            value='否',
                            inline=True,
                            inputClassName='mx-1',
                            labelClassName='me-2',
                        ),
                    ],width=2),
                    dbc.Col([
                        html.Label(['頂樓加蓋']),
                        dcc.RadioItems(
                            id='x-roof',
                            options=['是','否'],
                            value='否',
                            inline=True,
                            inputClassName='mx-1',
                            labelClassName='me-2',
                        ),
                    ],width=2)
                ]),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.Label(['建物樓高']),'  　',
                        dcc.Input(
                            id="x-building-height",
                            type='number',
                            value=1,
                            min=1,
                            step=1,
                            debounce=True,
                            style={'marginRight':'10px'}
                        ),'樓',
                    ],width=4),
                    dbc.Col([
                        html.Label(['所在樓高']),' 　 ',
                        dcc.Input(
                            id="x-floor-height",
                            type='number',
                            value=1,
                            min=1,
                            step=1,
                            debounce=True,
                            style={'marginRight':'10px'}
                        ),'樓',
                    ],width=4),
                    dbc.Col([
                        html.Label(['坪數']),'　 　　',
                        dcc.Input(
                            id="x-ping",
                            type='number',
                            value=1,
                            min=0.001,
                            step=0.001,
                            debounce=True,
                            style={'marginRight':'10px'}
                        ),'坪'
                    ],width=4),
                ]),
                dbc.Row([
                    
                    # dbc.Col([
                    #     html.Label(['距頂樓層數']),
                    #     dcc.Input(
                    #         id="",
                    #         type='number',
                    #         min=1,
                    #         step=1,
                    #         debounce=True
                    #     ),
                    # ],width=6),
                ]),
                html.Br(),
                html.H4(['價位資訊']),
                dbc.Row([
                    dbc.Col([
                        html.Label(['額外費用'],className='fw-bold'),
                        dcc.Checklist(
                            id='x-extra-cost',
                            options=['電費','水費','瓦斯','網路','第四台'],
                            value=['電費','水費','瓦斯','網路','第四台'],
                            inline=True,
                            className='m-2',
                            inputClassName='mx-1',
                            labelClassName='me-2',
                        )
                    ],width=6),
                    dbc.Col([
                        html.Label(['需要管理費'],className='fw-bold'),
                        dcc.RadioItems(
                            id='x-manage',
                            options=['是','否'],
                            value='否',
                            inputClassName='mx-1',
                            labelClassName='me-2',
                        ),
                    ],width=2),
                    dbc.Col([
                        html.Label(['月管理費'],className='fw-bold'),
                        dcc.Input(
                            id='x-manage-cost',
                            type='number',
                            value=0,
                            min=0,
                            step=100,
                            style={'marginRight':'10px'}
                        ),"元",
                    ],width=4),
                ]),
                html.Br(),
                html.H4(['環境、設備與限制']),
                dbc.Row([
                    dbc.Col([
                        html.Label(['生活機能'],className='fw-bold'),
                        dcc.Checklist(
                            id='x-environment',
                            options=['近學校','近公園','近百貨公司','近超商','近傳統市場','近夜市','近醫療機構'],
                            value=['近超商'],
                            inline=True,
                            inputClassName='mx-1',
                            labelClassName='me-2',
                        ),
                        html.Br(),
                        html.Label(['提供傢具'],className='fw-bold'),
                        dcc.Checklist(
                            id='x-furniture',
                            options=['床','衣櫃','桌子','椅子','沙發'],
                            value=['床','衣櫃','桌子','椅子'],
                            inline=True,
                            inputClassName='mx-1',
                            labelClassName='me-2',
                        ),
                        html.Br(),
                        html.Label(['提供設備'],className='fw-bold'),
                        dcc.Checklist(
                            id='x-equipment',
                            options=['電視','熱水器','冷氣','洗衣機','冰箱','網路','第四台','天然瓦斯'],
                            inline=True,
                            value=['熱水器','冷氣','洗衣機','網路'],
                            inputClassName='mx-1',
                            labelClassName='me-2',
                        ),
                    ])
                ]),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.Label(['身份限制'],className='fw-bold'),
                        dcc.RadioItems(
                            id='x-id',
                            options=['有','無'],
                            value='無',
                            inputClassName='mx-1',
                            labelClassName='me-2',
                        ),
                    ],width=3),
                    dbc.Col([
                        html.Label(['性別要求'],className='fw-bold'),
                        dcc.RadioItems(
                            id='x-sexaul',
                            options=['皆可','限男','限女'],
                            value='皆可',
                            inputClassName='mx-1',
                            labelClassName='me-2',
                        ),
                    ],width=3),
                    dbc.Col([
                        html.Label(['開伙'],className='fw-bold'),
                        dcc.RadioItems(
                            id='x-cook',
                            options=['可','不可'],
                            value='不可',
                            inputClassName='mx-1',
                            labelClassName='me-2',
                        ),
                    ],width=3),
                    dbc.Col([
                        html.Label(['養寵物'],className='fw-bold'),
                        dcc.RadioItems(
                            id='x-pet',
                            options=['可','不可'],
                            value='不可',
                            inputClassName='mx-1',
                            labelClassName='me-2',
                        ),
                    ],width=3)
                ]),
                html.Br(),
                html.Button(children='估價',id='run-button',n_clicks=0,className='px-3 py-1'),    
            ])
        ],width=5),
    ])
])




@app.callback([
    Output(component_id='x-vill', component_property='options'),
    Output(component_id='x-vill', component_property='value')
],  
    Input(component_id='x-district', component_property='value')
)
def update_output_div(town_name):
    if town_name=='東區':
        vill=dong_vill
        value=dong_vill[0]
    elif town_name=='中西區':
        vill=zhxi_vill
        value=zhxi_vill[0]
    elif town_name=='北區':
        vill=ba_vill
        value=ba_vill[0]
    elif town_name=='南區':
        vill=nan_vill
        value=nan_vill[0]
    elif town_name=='安平區':
        vill=anping_vill
        value=anping_vill[0]
    elif town_name=='安南區':
        vill=annan_vill
        value=annan_vill[0]
    elif town_name=='永康區':
        vill=yk_vill
        value=yk_vill[0]

    return vill,value


@app.callback(
    Output('predict-money','children'),
    Input('run-button','n_clicks'),      # 按鈕
    State('model-selection','value'),  # 模型選擇
    State('x-district','value'),        # 鄉鎮市區
    State('x-vill','value'),            # 村里
    State('x-building-type','value'),   # 建築類型
    State('x-room-type','value'),       # 物件類型
    State('x-parking','value'),         # 提供車位
    State('x-roof','value'),            # 頂樓加蓋
    State('x-building-height','value'), # 建物樓高
    State('x-floor-height','value'),    # 所在樓高
    State('x-ping','value'),            # 坪數
    State('x-extra-cost','value'),      # 額外費用
    State('x-manage','value'),          # 需要管理費
    State('x-manage-cost','value'),     # 月管理費
    State('x-environment','value'),     # 生活機能
    State('x-furniture','value'),       # 提供傢具
    State('x-equipment','value'),       # 提供設備
    State('x-id','value'),              # 身份限制
    State('x-sexaul','value'),          # 性別要求
    State('x-cook','value'),            # 開火
    State('x-pet','value'),             # 寵物
)
def get_parameters(button,
    model,district,vill,building,room,parking,roof,height,
    floor,ping,extra_cost,manage,manage_cost,environment,furniture,
    equipment,id,sexaul,cook,pet,
    ):
    print(button)
    env_list=['近學校','近公園','近百貨公司','近超商','近傳統市場','近夜市','近醫療機構']
    building_type_list=['公寓','透天','電梯大樓']
    room_type_list=['分租套房','整層住家','獨立套房','雅房']
    extra_cost_list=['電費','水費','瓦斯','網路','第四台']
    equ_fur_list=['桌子','椅子','電視','熱水器','冷氣','沙發','洗衣機','衣櫃','冰箱','網路','第四台','天然瓦斯']
    sexaul_list=['皆可','限男','限女']

    equ_fur=equipment+furniture
    district_para=[1 if district==i else 0 for i in town_vill]
    vill_para=[1 if vill==i else 0 for i in all_vill]
    
    manage_para=bool2int(manage)
    parking_para=bool2int(parking)
    roof_para=bool2int(roof)
    id_para=bool2int(id)
    cook_para=bool2int(cook)
    pet_para=bool2int(pet)
    sexaul_para=[]
    for i in sexaul_list:
        if i in sexaul:
            sexaul_para.append(1)
        else:
            sexaul_para.append(0)
    if sexaul_para[0]==1:
        sexaul_if_para=[1,0]
    else:
        sexaul_if_para=[0,1]
    # 產權登記(懶得用的，先固定數字)
    right_para=[0,1]
    height2roof=int(height)-int(floor)
    
    building_para=[]
    for i in room_type_list:
        if i==building:
            building_para.append(1)
        else:
            building_para.append(0)
    
    room_para=[]
    for i in room_type_list:
        if i==room:
            room_para.append(1)
        else:
            room_para.append(0)
    
    extra_cost_para=[]
    for i in extra_cost_list:
        if i in extra_cost:
            extra_cost_para.append(0)
            extra_cost_para.append(1)
        elif i not in extra_cost:
            extra_cost_para.append(1)
            extra_cost_para.append(0)
    env_para=[]
    for i in env_list:
        if i in environment:
            env_para.append(0)
            env_para.append(1)
        elif i not in environment:
            env_para.append(1)
            env_para.append(0)
    equ_fur_para=[]
    for i in equ_fur_list:
        if i in equ_fur:
            equ_fur_para.append(0)
            equ_fur_para.append(1)
        elif i not in equ_fur:
            equ_fur_para.append(1)
            equ_fur_para.append(0)
    final_para=[manage_cost,floor,height,height2roof,ping]+district_para+manage_para+parking_para+building_para+room_para+roof_para+extra_cost_para+env_para+id_para+sexaul_if_para+sexaul_para+cook_para+pet_para+right_para+equ_fur_para+vill_para
    print(final_para)
    print(len(final_para))

    if model=='線性迴歸':
        x =lr_model.predict([final_para])
        x= list(map(lambda x :str(x) ,x.round(2)))
        y=str(float(x[0])*ping)
        return f"以上條件預估單坪價格為 {x[0]} 坪/元 租金為 {y} 元"
        
    elif model=='隨機迴歸森林':
        x =rd_model.predict([final_para])
        x= list(map(lambda x :str(x) ,x.round(2)))
        y=str(float(x[0])*ping)
        return f"以上條件預估單坪價格為 {x[0]} 坪/元 租金為 {y} 元"
    elif model=='極限梯度提升法':
        x =xgb_model.predict(np.array([final_para]))
        x= list(map(lambda x :str(x) ,x.round(2)))
        y=str(float(x[0])*ping)
        return f"以上條件預估單坪價格為 {x[0]} 坪/元 租金為 {y} 元"

@app.callback(
    Output('map-part', 'children'),
    Input('x-vill', 'value'),
)
def update_map(vill_name):
    map_update=make_map(vill_name)
    return map_update


if __name__=='__main__':
    app.run_server(host='0.0.0.0', port=9000)
    # app.run_server(debug=True)