<?php

namespace MountainTales\Packing\Model\ResourceModel\{{ model }};

use Magento\Framework\Model\ResourceModel\Db\Collection\AbstractCollection;
use MountainTales\Packing\Model\ResourceModel\{{ resource_model }} as {{ resource_model }}Resource;
use MountainTales\Packing\Model\{{ model }};

/**
 * Class {{ model }} Collection
 *
 * @package   MountainTales\Packing\Model\ResourceModel\{{ model }}
 * @author    Jaep Cuperus <jaep@mountain-it.nl>
 * @copyright 24-4-19
 * @license   https://www.mountain-it.nl Commercial License
 */
class Collection extends AbstractCollection
{
    protected $_idFieldName = '{{ primary_key }}';

    /**
     * {{ model }} collection constructor
     */
    protected function _construct()
    {
        $this->_init({{ model }}::class, {{ resource_model }}Resource::class);
    }
}