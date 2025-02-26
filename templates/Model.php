<?php

namespace MountainTales\Packing\Model;

use Magento\Framework\Model\AbstractModel;
{% if columns %}use MountainTales\Packing\Api\Data\{{ model }}Interface;{% endif %}
use MountainTales\Packing\Model\ResourceModel\{{ resource_model }} as {{ resource_model }}Resource;

/**
 * Class {{ model }}
 *
 * @package   MountainTales\Packing\Model
 * @author    Jaep Cuperus <jaep@mountain-it.nl>
 * @copyright 24-4-19
 * @license   https://www.mountain-it.nl Commercial License
 */
class {{ model }} extends AbstractModel {% if columns %}implements {{ model }}Interface{% endif %}
{
    /**
     * {{ model }} constructor
     */
    protected function _construct()
    {
        $this->_init({{ resource_model }}Resource::class);
    }
{% for column in columns %}
    /**
     * {@inheritDoc}
     */
    public function get{{ column.pascal }}()
    {
        return $this->getData(self::{{ column.name.upper() }});
    }

    /**
     * {@inheritDoc}
     */
    public function set{{ column.pascal }}(${{ column.camel }})
    {
        return $this->setData(self::{{ column.name.upper() }}, ${{ column.camel }});
    }
{% endfor %}
}